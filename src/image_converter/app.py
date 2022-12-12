import logging
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.timing import add_timing_middleware

from src.config.config import STATIC_FILE
from src.image_converter.views.router import (
    bmp_router,
    heic_router,
    jpg_router,
    png_router,
    psd_router,
    svg_router,
    tiff_router,
    vsd_router,
    vsdx_router,
    webp_router,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
add_timing_middleware(
    app, record=logger.info, prefix="/v1/tool/image", exclude="untimed"
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(jpg_router, tags=["JPG"], prefix="/v1/tool/image")
app.include_router(png_router, tags=["PNG"], prefix="/v1/tool/image")
app.include_router(webp_router, tags=["WEBP"], prefix="/v1/tool/image")
app.include_router(psd_router, tags=["PSD"], prefix="/v1/tool/image")
app.include_router(tiff_router, tags=["TIFF"], prefix="/v1/tool/image")
app.include_router(svg_router, tags=["SVG"], prefix="/v1/tool/image")
app.include_router(vsd_router, tags=["VSD"], prefix="/v1/tool/image")
app.include_router(vsdx_router, tags=["VSDX"], prefix="/v1/tool/image")
app.include_router(bmp_router, tags=["BMP"], prefix="/v1/tool/image")
app.include_router(heic_router, tags=["HEIC"], prefix="/v1/tool/image")


@app.on_event("startup")
async def startup_event():
    os.makedirs(STATIC_FILE, exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Welcome to the Image Converter API"}


if __name__ == "__main__":
    uvicorn.run("src.image_converter.app:app", host="127.0.0.1", port=6063)
