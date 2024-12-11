from pydantic import BaseModel, EmailStr


class SafeUser(BaseModel):
    email: EmailStr
