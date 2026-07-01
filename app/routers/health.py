# app/routers/health.py
"""
Endpoint بررسی سلامت سرویس.
ورودی: ندارد.
خروجی: JSON {'status': 'ok'}.
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}