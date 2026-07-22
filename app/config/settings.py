import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

# ---------------------------------------------------
# Load .env
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

print(f"BASE_DIR: {BASE_DIR}")

dotenv_file = BASE_DIR / ".env"

print(f".env exists: {dotenv_file.exists()}")
print(f".env path: {dotenv_file}")

load_dotenv(dotenv_path=dotenv_file, override=True)

print("BEDROCK_MODEL_ID =", os.getenv("BEDROCK_MODEL_ID"))

# ---------------------------------------------------
# Settings
# ---------------------------------------------------

@dataclass
class Settings:
    AWS_REGION: str
    MODEL_ID: str
    MAX_TOKENS: int
    TEMPERATURE: float
    TOP_P: float


settings = Settings(
    AWS_REGION=os.getenv("AWS_REGION", "us-east-1"),
    MODEL_ID=os.getenv("BEDROCK_MODEL_ID"),
    MAX_TOKENS=int(os.getenv("MAX_TOKENS", "512")),
    TEMPERATURE=float(os.getenv("TEMPERATURE", "0.5")),
    TOP_P=float(os.getenv("TOP_P", "0.9")),
)

if not settings.MODEL_ID:
    raise ValueError("BEDROCK_MODEL_ID is not configured")