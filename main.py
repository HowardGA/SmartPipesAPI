from fastapi import FastAPI
from app.api.router import router as api_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to SmartPipes!"}

# Mount API routers
app.include_router(api_router, prefix="/api")


