import os
from pathlib import Path
from dotenv import load_dotenv

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(PROJECT_ROOT / ".env")

# Application configuration
BASE_URL = os.getenv(
    "BASE_URL",
    "https://practicesoftwaretesting.com/"
)

# Browser configuration
BROWSER = os.getenv("BROWSER", "chrome").lower()

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

# Wait configuration
EXPLICIT_WAIT_SECONDS = int(
    os.getenv("EXPLICIT_WAIT_SECONDS", "10")
)