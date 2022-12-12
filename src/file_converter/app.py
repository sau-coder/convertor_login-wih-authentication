import logging
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.timing import add_timing_middleware

from src.config.config import STATIC_FILE
from src.file_converter.views.router import (
    csv_router,
    excel_router,
    json_router,
    tsv_router,
    xml_router,
    yaml_router,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
add_timing_middleware(
    app, record=logger.info, prefix="/v1/tool/file", exclude="untimed"
)
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(csv_router, tags=["CSV"], prefix="/v1/tool/file")
app.include_router(tsv_router, tags=["TSV"], prefix="/v1/tool/file")
app.include_router(excel_router, tags=["EXCEL"], prefix="/v1/tool/file")
app.include_router(json_router, tags=["JSON"], prefix="/v1/tool/file")
app.include_router(xml_router, tags=["XML"], prefix="/v1/tool/file")
app.include_router(yaml_router, tags=["YAML"], prefix="/v1/tool/file")


@app.on_event("startup")
async def startup_event():
    os.makedirs(STATIC_FILE, exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Welcome to the File Converter API"}


if __name__ == "__main__":
    uvicorn.run("src.file_converter.app:app", host="127.0.0.1", port=6062)
