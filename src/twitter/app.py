import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.timing import add_timing_middleware

from src.twitter.views.router import tweet_shcreenshot_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
add_timing_middleware(
    app, record=logger.info, prefix="/v1/tool/tweet", exclude="untimed"
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tweet_shcreenshot_router, tags=["TWEET"], prefix="/v1/tool/tweet")


@app.get("/")
async def root():
    return {"message": "Welcome to the Tweet to Image Genaration API"}
