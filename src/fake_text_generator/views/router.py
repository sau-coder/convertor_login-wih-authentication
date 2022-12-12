from fastapi import APIRouter, Form, status
from fastapi.responses import JSONResponse

from src.fake_text_generator.controller.Text_Generation_Contoller import (
    Text_Generation_Contoller,
)
from src.fake_text_generator.utils.Fake_Text_Generation_Types import (
    Fake_Text_Generation_Types,
)

fake_text_router = APIRouter()


@fake_text_router.post("/fake_text")
def fake_text_generator(text_generation_type: Fake_Text_Generation_Types = Form(None)):
    try:

        text_generation_controller_object = Text_Generation_Contoller(
            conversion_type=text_generation_type
        )
        result = text_generation_controller_object.get_fake_text()

        return JSONResponse(
            content={
                "success": True,
                "message": "Text Generated Successfully",
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
