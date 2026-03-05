import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "LoL Esports Support AI"
    VERSION: str = "1.0.0"
    
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    
    MODEL_NAME: str = os.getenv("MODEL_NAME", "llama3.1:8b")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", 0.2))
    
    CHROMA_PERSIST_DIR: str = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")

settings = Settings()