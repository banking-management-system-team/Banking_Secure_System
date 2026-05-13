from dotenv import load_dotenv
from pathlib import Path
import os

root_dir = Path(__file__).resolve().parents[2]
load_dotenv(root_dir / ".env", override=True, encoding="utf-8-sig")


class Settings:

    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise RuntimeError(
            "DATABASE_URL is not set. Set it in .env for Supabase."
        )

    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        raise RuntimeError(
            "SECRET_KEY is not set. Set it in .env."
        )

    ALGORITHM = os.getenv("ALGORITHM", "HS256")

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
    )


settings = Settings()