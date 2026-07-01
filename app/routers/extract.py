# app/routers/extract.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import logging
from ..extractors import process_text
from ..models import loader   # import کل ماژول، نه متغیرها

router = APIRouter()
logger = logging.getLogger(__name__)

class AdText(BaseModel):
    text: str = Field(..., min_length=1, description="متن آگهی")

@router.post("/extract")
async def extract(input: AdText):
    logger.info(f"Received text: {input.text[:100]}...")
    # اطمینان از بارگذاری مدل (اگر قبلاً نشده باشد)
    if loader.tokenizer is None:
        loader.load_model()
    result = process_text(input.text, loader.tokenizer, loader.model, loader.device)
    logger.info(f"Extracted result: {result}")
    return result

@router.post("/parse-ad")
async def parse_ad(input: AdText):
    return await extract(input)