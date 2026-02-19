from fastapi import APIRouter

router = APIRouter()

@router.get("/transactions/test")
def get_transactions():
    return {"message": "Transactions endpoint is working!"}
