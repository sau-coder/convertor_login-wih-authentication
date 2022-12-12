import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.timing import add_timing_middleware

from src.config.config import STATIC_FILE
from src.watermark.views.router import add_watermark_router

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

add_timing_middleware(
    app, record=logger.info, prefix="/v1/tool/watermark", exclude="untimed"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    add_watermark_router, tags=["WATERMARK"], prefix="/v1/tool/watermark"
)


@app.on_event("startup")
async def startup_event():
    os.makedirs(STATIC_FILE, exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Welcome to the Watermark Adder on Image API"}
