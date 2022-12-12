import logging
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.timing import add_timing_middleware

from src.config.config import STATIC_FILE
from src.video_converter.views.router import (
    avi_router,
    mkv_router,
    mov_router,
    mp4_router,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
add_timing_middleware(
    app, record=logger.info, prefix="/v1/tool/video", exclude="untimed"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(mp4_router, tags=["MP4"], prefix="/v1/tool/video")
app.include_router(mov_router, tags=["MOV"], prefix="/v1/tool/video")
app.include_router(mkv_router, tags=["MKV"], prefix="/v1/tool/video")
app.include_router(avi_router, tags=["AVI"], prefix="/v1/tool/video")


@app.on_event("startup")
async def startup_event():
    os.makedirs(STATIC_FILE, exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Welcome to the Video Converter API"}


if __name__ == "__main__":
    uvicorn.run("src.video_converter.app:app", host="127.0.0.1", port=6064)
