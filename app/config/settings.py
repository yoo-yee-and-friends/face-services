import os
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv(override=True)

class Settings:
    DATABASE_HOST: str = os.getenv("DATABASE_HOST")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
    DATABASE_USER: str = os.getenv("DATABASE_USER")
    DATABASE_PW: str = os.getenv("DATABASE_PW")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT")
    DATABASE_URL: str = f"postgresql://{DATABASE_USER}:{DATABASE_PW}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    DEBUG=True
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DROPBOX_ACCESS_TOKEN: str = os.getenv("DROPBOX_ACCESS_TOKEN")
    DLIB_FACE_RECOGNITION_MODEL_FILE: str = os.getenv("DLIB_FACE_RECOGNITION_MODEL_FILE")
    SHAPE_PREDICTOR_MODEL_FILE: str =os.getenv("SHAPE_PREDICTOR_MODEL_FILE")
    DROPBOX_BASE_URL: str = os.getenv("DROPBOX_BASE_URL")
    MODEL_DIR: str = os.getenv("MODEL_DIR")
    DLIB_FACE_RECOGNITION_MODEL_PATH: str = f"{MODEL_DIR}/{DLIB_FACE_RECOGNITION_MODEL_FILE}"
    SHAPE_PREDICTOR_MODEL_PATH: str = f"{MODEL_DIR}/{SHAPE_PREDICTOR_MODEL_FILE}"

settings = Settings()
