from fastapi import APIRouter, File, Form, UploadFile, status
from fastapi.responses import JSONResponse

from src.audio_converter.controller.Audio_Conversion_Controller import (
    Audio_Conversion_Controller,
)
from src.audio_converter.utils.Audio_Conversion_Types import (
    AAC_Conversion_Types,
    Conversion_Types,
    M4A_Conversion_Types,
    MP3_Conversion_Types,
    OGG_Conversion_Types,
    WAV_Conversion_Types,
)
from src.utils.extension_checker import extension_checker
from src.utils.file_download import save_file
from src.utils.remove_static_files import remove_files

mp3_router = APIRouter()


@mp3_router.post("/mp3")
def mp3_conversions(
    conversion_type: MP3_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "mp3":

            mp3_controller_object = Audio_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.mp3,
            )
            s3_url = mp3_controller_object.convert_file()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "File Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Document File",
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


wav_router = APIRouter()


@wav_router.post("/wav")
def wav_conversions(
    conversion_type: WAV_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "wav":

            wav_controller_object = Audio_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.wav,
            )
            s3_url = wav_controller_object.convert_file()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "File Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Document File",
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


ogg_router = APIRouter()


@ogg_router.post("/ogg")
def ogg_conversions(
    conversion_type: OGG_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "ogg":

            ogg_controller_object = Audio_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.ogg,
            )
            s3_url = ogg_controller_object.convert_file()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "File Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Document File",
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


aac_router = APIRouter()


@aac_router.post("/aac")
def aac_conversions(
    conversion_type: AAC_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "aac":

            aac_controller_object = Audio_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.aac,
            )
            s3_url = aac_controller_object.convert_file()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "File Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Document File",
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


m4a_router = APIRouter()


@m4a_router.post("/m4a")
def m4a_conversions(
    conversion_type: M4A_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "m4a":

            m4a_controller_object = Audio_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.m4a,
            )
            s3_url = m4a_controller_object.convert_file()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "File Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Document File",
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
