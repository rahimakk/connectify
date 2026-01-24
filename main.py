from fastapi import FastAPI
from models import User
from database import engine,Base
from auth import router as auth_router
app = FastAPI(title="Connectify API")
app.include_router(auth_router)
@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "message": "Connectify backend is running 🚀"
    }

Base.metadata.create_all(bind=engine)
