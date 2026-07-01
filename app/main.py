# app/main.py
"""
ورودی اصلی FastAPI : راه‌اندازی سرور، تنظیم لاگ، بارگذاری مدل و تعریف روت‌ها.
ورودی: از طریق خط فرمان یا اجرای مستقیم.
خروجی: سرور روی HOST:PORT راه‌اندازی می‌شود.
"""

import logging
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from .config import HOST, PORT, LOG_FILE
from .models.loader import load_model   # فقط تابع بارگذاری
from .routers.extract import router as extract_router
from .routers.health import router as health_router

# -------------------- تنظیم لاگ --------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# -------------------- بارگذاری مدل --------------------
load_model()   # این کار متغیرهای سراسری loader را پر می‌کند

# -------------------- اپلیکیشن FastAPI --------------------
app = FastAPI(title="Real Estate Info Extractor", version="1.0", docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(extract_router)
app.include_router(health_router)

# روت اصلی (HTML)
STATIC_DIR = Path(__file__).parent / "static"
@app.get("/", response_class=HTMLResponse)
async def index():
    index_file = STATIC_DIR / "index.html"
    if not index_file.exists():
        return HTMLResponse(content="index.html not found", status_code=404)
    return index_file.read_text(encoding="utf-8")

# -------------------- اجرا --------------------
if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting server on {HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT)