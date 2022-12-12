from fastapi import APIRouter, Form, status
from fastapi.responses import JSONResponse

from src.twitter.controller.Tweet_Screenshots_Controller import (
    Tweet_Screenshot_Controller,
)

tweet_shcreenshot_router = APIRouter()


@tweet_shcreenshot_router.post("/tweet_shcreenshot")
def tweet_shcreenshot_generator(tweet_url: str = Form(None)):
    try:

        screenshot_controller = Tweet_Screenshot_Controller(tweet_url)
        result = screenshot_controller.get_base_64_of_tweet()

        return JSONResponse(
            content={
                "success": True,
                "message": "Tweet screenshot generated successfully",
                "error": None,
                "data": result,
            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Something Went Wrong",
                "error": str(e),
                "data": None,
            },
        )
