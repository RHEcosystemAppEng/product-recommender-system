from fastapi import APIRouter
from typing import List
from backend.models import CheckoutRequest, Order
from datetime import datetime

router = APIRouter()

@router.post("/checkout", response_model=Order)
def checkout(request: CheckoutRequest):
    return Order(
        order_id=1,
        user_id=request.user_id,
        items=request.items,
        total_amount=199.99,
        order_date=datetime.now(),
        status="processing"
    )

@router.get("/orders/{user_id}", response_model=List[Order])
def get_order_history(user_id: int):
    return []
