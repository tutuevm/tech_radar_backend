from dotenv import load_dotenv
from pydantic import BaseModel
from pathlib import Path
import os
from math import pi
from pydantic_settings import BaseSettings

load_dotenv()
BASE_DIR = Path(__file__).parent.parent


class AuthSettings(BaseModel):
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30


class RadarSettings(BaseModel):
    RADIUS: int = 400
    LEVEL_RANGES: dict = {
        "Adopt": [30, 60, 80],
        "Trial": [120, 150, 180],
        "Assess": [200, 250, 300],
        "Hold": [310, 360, 400],
    }
    QUARTER_RANGES: dict = {
        "Languages and frameworks": [pi, 3 * pi / 2],
        "Data management": [3 * pi / 2, 2 * pi],
        "Tools": [pi / 2, pi],
        "Platforms and infrastructure": [0, pi / 2],
    }


class SSLSettings(BaseModel):
    private_jwt_key: Path = BASE_DIR / "crt" / "private.pem"
    public_jwt_key: Path = BASE_DIR / "crt" / "public.pem"


class DataBaseSettings(BaseModel):
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: str = os.environ.get("DB_PORT")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASS: str = os.environ.get("DB_PASS")


class Settings(BaseSettings):
    API_TITLE: str = "TECH RADAR"
    API_DESCRIPTION: str = ""
    API_VERSION: str = "0.0.1"
    DB_Settings: DataBaseSettings = DataBaseSettings()
    SSL_Settings: SSLSettings = SSLSettings()
    AUTH_SETTINGS: AuthSettings = AuthSettings()
    RADAR_SETTINGS: RadarSettings = RadarSettings()


settings = Settings()
