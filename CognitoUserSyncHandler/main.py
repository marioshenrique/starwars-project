import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("users")


def register_user(user_id: str, email: str):
    try:
        response = table.scan(
            FilterExpression = "email = :email",
            ExpressionAttributeValues = {":email": email}
        )
        logger.info(f"Response: {response}")
        if response.get("Items"):
            logger.warning(f"Email {email} is already registered. Registration ignored.")
            raise Exception("Email already exists.")
        table.put_item(
            Item={
                "user_id": user_id,
                "email": email,
                "confirmed": False,
                "created_at": datetime.utcnow().isoformat(),
            },
            ConditionExpression="attribute_not_exists(user_id)",
        )
        logger.info(f"Registered user {user_id}!")
        return {"message": "User registered successfully."}

    except ClientError as e:
        logger.error(f"Error registering user {user_id}: {e}")
        raise Exception("Failed to register user.")

def confirm_user(user_id):
    try:
        table.update_item(
            Key={"user_id": user_id},
            UpdateExpression = "set confirmed = :c",
            ExpressionAttributeValues = {":c": True}
        )
        logger.info(f"User {user_id} confirmed successfully!")
        return {"message": "User confirmed successfully."}
    except ClientError as e:
        logger.error(f"Error confirming user {user_id}: {e}")
        raise Exception("Failed to confirm user.")


def lambda_handler(event, context):
    try:
        trigger_source = event.get("triggerSource", "")
        user_id = event.get("userName")
        email = event.get("request", {}).get("userAttributes", {}).get("email")
        logger.info(f"trigger_source: {trigger_source}")
        logger.info(f"user_id: {user_id}")
        logger.info(f"email: {email}")
        logger.info(f"Event: {event}")

        if not user_id or not email:
            logger.error("Invalid event: Missing 'user_id' or 'email'.")
            raise ValueError("Invalid event.")

        if trigger_source == "PreSignUp_SignUp":
            logger.info("Running PreSignUp...")
            register_user(user_id, email)
            return event

        elif trigger_source == "PostConfirmation_ConfirmSignUp":
            logger.info("Running PostConfirmation...")
            confirm_user(user_id)
            return event

        else:
            logger.warning(f"Trigger não suportado: {trigger_source}")
            return {"statusCode": 400}

    except Exception as e:
        logger.error(f"Error: {e}")
        raise Exception(e)
