from fastapi import FastAPI
from app.routes import transactions

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

app.include_router(transactions.router)