import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.timing import add_timing_middleware

from src.fake_text_generator.views.router import fake_text_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
add_timing_middleware(
    app, record=logger.info, prefix="/v1/tool/text", exclude="untimed"
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fake_text_router, tags=["TEXT"], prefix="/v1/tool/text")


@app.get("/")
async def root():
    return {"message": "Welcome to the Fake Text Generator API"}
