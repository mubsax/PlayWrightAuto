import os
from pathlib import Path
from dotenv import load_dotenv

CONFIG_DIR = Path(__file__).resolve().parent
dotenv_path = CONFIG_DIR / ".env"
load_dotenv(dotenv_path=dotenv_path)

class Config:
    BASE_URL = "https://app.sibme.com"
    LOGIN_URL = f"{BASE_URL}/home/login"
    DEFAULT_TIMEOUT = 30000

    USER = os.getenv("TEST_USER")
    PASS = os.getenv("TEST_PASS")