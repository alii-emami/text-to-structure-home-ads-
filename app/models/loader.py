# app/models/loader.py
"""
بارگذاری مدل NER و توکنایزر از پوشه محلی.
ورودی: هیچ (از config مسیر را می‌خواند).
خروجی: توکنایزر، مدل و دستگاه (device) به صورت global.
"""
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
from ..config import MODEL_DIR

# متغیرهای سراسری (ابتدا None)
tokenizer = None
model = None
device = None

def load_model():
    global tokenizer, model, device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Loading model from {MODEL_DIR}")
    tokenizer = AutoTokenizer.from_pretrained(str(MODEL_DIR), local_files_only=True)
    model = AutoModelForTokenClassification.from_pretrained(str(MODEL_DIR), local_files_only=True)
    model.to(device)
    model.eval()
    print("✅ Model and tokenizer loaded successfully.")
    return tokenizer, model, device