import logging
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")


def setup_logging():
    logging.basicConfig(level=logging.ERROR)
    logger = logging.getLogger()
    return logger
