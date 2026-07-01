# app/config.py
"""
تنظیمات مسیرها و پورت پروژه.
ورودی: ندارد.
خروجی: متغیرهای مسیر (BASE_DIR, MODEL_DIR, LOG_DIR, LOG_FILE) و HOST, PORT.
"""


import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
MODEL_DIR = BASE_DIR / "model"
LOG_DIR = Path(__file__).parent / "logs"
LOG_FILE = LOG_DIR / "app.log"

# اطمینان از وجود پوشه لاگ
os.makedirs(LOG_DIR, exist_ok=True)

# تنظیمات سرور
HOST = "127.0.0.1"
PORT = 8000