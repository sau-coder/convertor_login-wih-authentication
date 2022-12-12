from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import JSONResponse

from src.watermark.conversion.add_watermark import Watermark_Adder

add_watermark_router = APIRouter()


@add_watermark_router.post("/add_watermark")
async def watermark_adder(
    image: UploadFile = File(None),
    watermark: UploadFile = File(None),
):
    try:

        image = await image.read()
        watermark = await watermark.read()
        adder_obj = Watermark_Adder(image, watermark)
        ret_base_64 = adder_obj.add_watermark()

        # Saving the response
        return JSONResponse(
            content={
                "success": True,
                "message": "Watermark successfully added on image",
                "error": None,
                "data": ret_base_64.decode("utf-8"),
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
