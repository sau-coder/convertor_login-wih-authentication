from fastapi import APIRouter, File, Form, UploadFile, status
from fastapi.responses import JSONResponse

from src.utils.extension_checker import extension_checker
from src.utils.file_download import save_file
from src.utils.remove_static_files import remove_files
from src.video_converter.controller.Video_Conversion_Controller import (
    Video_Conversion_Controller,
)
from src.video_converter.utils.Video_Conversion_Types import (
    AVI_Conversion_Types,
    Conversion_Types,
    MKV_Conversion_Types,
    MOV_Conversion_Types,
    MP4_Conversion_Types,
)

mp4_router = APIRouter()


@mp4_router.post("/mp4")
def mp4_conversions(
    conversion_type: MP4_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "mp4":

            mp4_controller_object = Video_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.mp4,
            )
            s3_url = mp4_controller_object.convert_video()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Video Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static videos if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Video File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static files if error occurs
        remove_files(folder_name)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Something Went Wrong",
                "error": str(e),
                "data": None,
            },
        )


mkv_router = APIRouter()


@mkv_router.post("/mkv")
def mkv_conversions(
    conversion_type: MKV_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "mkv":

            mkv_controller_object = Video_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.mkv,
            )
            s3_url = mkv_controller_object.convert_video()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Video Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static videos if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Video File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static files if error occurs
        remove_files(folder_name)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Something Went Wrong",
                "error": str(e),
                "data": None,
            },
        )


avi_router = APIRouter()


@avi_router.post("/avi")
def avi_conversions(
    conversion_type: AVI_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "avi":

            avi_controller_object = Video_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.avi,
            )
            s3_url = avi_controller_object.convert_video()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Video Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static videos if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Video File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static files if error occurs
        remove_files(folder_name)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Something Went Wrong",
                "error": str(e),
                "data": None,
            },
        )


mov_router = APIRouter()


@mov_router.post("/mov")
def mov_conversions(
    conversion_type: MOV_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "mov":

            mov_controller_object = Video_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.mov,
            )
            s3_url = mov_controller_object.convert_video()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Video Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static videos if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Video File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static files if error occurs
        remove_files(folder_name)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Something Went Wrong",
                "error": str(e),
                "data": None,
            },
        )
