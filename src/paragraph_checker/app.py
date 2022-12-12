import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.timing import add_timing_middleware

from src.paragraph_checker.views.router import paragraph_stats

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

add_timing_middleware(
    app, record=logger.info, prefix="/v1/tool/paragraph", exclude="untimed"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(paragraph_stats, tags=["PARAGRAPH"], prefix="/v1/tool/paragraph")


@app.get("/")
async def root():
    return {"message": "Welcome to the Paragraph Checker API"}
