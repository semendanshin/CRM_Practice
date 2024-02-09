import os

from dotenv import load_dotenv

load_dotenv()


JWT_SECRET = os.environ.get("JWT_SECRET")
ACCESS_EXPIRE_DAYS = os.environ.get("ACCESS_EXPIRE_DAYS")
REFRESH_EXPIRE_DAYS = os.environ.get("REFRESH_EXPIRE_DAYS")
