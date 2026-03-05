from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="LoL Esports Support AI",
    description="API inteligente com RAG para suporte sobre League of Legends competitivo",
    version="1.0.0"
)

app.include_router(router)