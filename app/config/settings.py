import os
from pathlib import Path
from dotenv import load_dotenv

# Resolve the project root
BASE_DIR = Path(__file__).resolve().parents[2]

print(f"BASE_DIR: {BASE_DIR}")

dotenv_file = BASE_DIR / ".env"
print(f".env exists: {dotenv_file.exists()}")
print(f".env path: {dotenv_file}")

load_dotenv(dotenv_path=dotenv_file, override=True)

print("BEDROCK_MODEL_ID =", os.getenv("BEDROCK_MODEL_ID"))


class Settings:
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    MODEL_ID = os.getenv("BEDROCK_MODEL_ID")

    if not MODEL_ID:
        raise ValueError("BEDROCK_MODEL_ID is not configured")


settings = Settings()