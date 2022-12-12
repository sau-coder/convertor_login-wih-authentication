import logging
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.timing import add_timing_middleware

from src.config.config import STATIC_FILE
from src.document_converter.views.router import doc_router, pdf_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

add_timing_middleware(app, record=logger.info, prefix="/v1/tool/doc", exclude="untimed")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(pdf_router, tags=["PDF"], prefix="/v1/tool/doc")
app.include_router(doc_router, tags=["DOC"], prefix="/v1/tool/doc")


@app.on_event("startup")
async def startup_event():
    os.makedirs(STATIC_FILE, exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Welcome to the Document Converter API"}


if __name__ == "__main__":
    uvicorn.run("src.document_converter.app:app", host="127.0.0.1", port=6061)
