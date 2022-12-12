from fastapi import APIRouter, File, Form, UploadFile, status
from fastapi.responses import JSONResponse

from src.image_converter.controller.Image_Conversion_Controller import (
    Image_Conversion_Controller,
)
from src.image_converter.utils.Image_Conversion_Types import (
    BMP_Conversion_Types,
    Conversion_Types,
    HEIC_Conversion_Types,
    JPG_Conversion_Types,
    PNG_Conversion_Types,
    PSD_Conversion_Types,
    SVG_Conversion_Types,
    TIFF_Conversion_Types,
    VSD_Conversion_Types,
    VSDX_Conversion_Types,
    WEBP_Conversion_Types,
)
from src.utils.extension_checker import extension_checker
from src.utils.file_download import save_file
from src.utils.remove_static_files import remove_files

jpg_router = APIRouter()


@jpg_router.post("/jpg")
def jpg_conversions(
    conversion_type: JPG_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "jpg":

            jpg_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.jpg,
            )
            s3_url = jpg_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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


png_router = APIRouter()


@png_router.post("/png")
def png_conversions(
    conversion_type: PNG_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "png":

            png_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.png,
            )
            s3_url = png_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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


webp_router = APIRouter()


@webp_router.post("/webp")
def webp_conversions(
    conversion_type: WEBP_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "webp":

            webp_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.webp,
            )
            s3_url = webp_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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


tiff_router = APIRouter()


@tiff_router.post("/tiff")
def tiff_conversions(
    conversion_type: TIFF_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "tiff":

            tiff_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.tiff,
            )
            s3_url = tiff_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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


psd_router = APIRouter()


@psd_router.post("/psd")
def psd_conversions(
    conversion_type: PSD_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "psd":

            psd_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.psd,
            )
            s3_url = psd_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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


svg_router = APIRouter()


@svg_router.post("/svg")
def svg_conversions(
    conversion_type: SVG_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "svg":

            svg_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.svg,
            )
            s3_url = svg_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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


vsd_router = APIRouter()


@vsd_router.post("/vsd")
def vsd_conversions(
    conversion_type: VSD_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "vsd":

            vsd_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.vsd,
            )
            s3_url = vsd_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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


vsdx_router = APIRouter()


@vsdx_router.post("/vsdx")
def vsdx_conversions(
    conversion_type: VSDX_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "vsdx":

            vsdx_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.vsdx,
            )
            s3_url = vsdx_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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


bmp_router = APIRouter()


@bmp_router.post("/bmp")
def bmp_conversions(
    conversion_type: BMP_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "bmp":

            bmp_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.bmp,
            )
            s3_url = bmp_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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


heic_router = APIRouter()


@heic_router.post("/heic")
def heic_conversions(
    conversion_type: HEIC_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "heic":

            heic_controller_object = Image_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.heic,
            )
            s3_url = heic_controller_object.convert_image()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Image Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static image files if error occurs
            remove_files(folder_name)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": "Please Provide Valid Image File",
                    "error": "Not Valid File Format",
                    "data": None,
                },
            )

    except Exception as e:
        # Remove static image files if error occurs
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
