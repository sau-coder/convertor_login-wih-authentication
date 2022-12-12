import logging
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.timing import add_timing_middleware

from src.audio_converter.views.router import (
    aac_router,
    m4a_router,
    mp3_router,
    ogg_router,
    wav_router,
)
from src.config.config import STATIC_FILE

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

add_timing_middleware(
    app, record=logger.info, prefix="/v1/tool/audio", exclude="untimed"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mp3_router, tags=["MP3"], prefix="/v1/tool/audio")
app.include_router(m4a_router, tags=["M4A"], prefix="/v1/tool/audio")
app.include_router(aac_router, tags=["AAC"], prefix="/v1/tool/audio")
app.include_router(wav_router, tags=["WAV"], prefix="/v1/tool/audio")
app.include_router(ogg_router, tags=["OGG"], prefix="/v1/tool/audio")


@app.on_event("startup")
async def startup_event():
    os.makedirs(STATIC_FILE, exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Welcome to the Audio Converter API"}


if __name__ == "__main__":
    uvicorn.run("src.audio_converter.app:app", host="127.0.0.1", port=6065)
