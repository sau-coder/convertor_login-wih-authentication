from fastapi import APIRouter, File, Form, UploadFile, status
from fastapi.responses import JSONResponse

from src.file_converter.controller.File_Conversion_Controller import (
    File_Conversion_Controller,
)
from src.file_converter.utils.File_Conversion_Types import (
    Conversion_Types,
    CSV_Conversion_Types,
    EXCEL_Conversion_Types,
    JSON_Conversion_Types,
    TSV_Conversion_Types,
    XML_Conversion_Types,
    YAML_Conversion_Types,
)
from src.utils.extension_checker import extension_checker
from src.utils.file_download import save_file
from src.utils.remove_static_files import remove_files

csv_router = APIRouter()


@csv_router.post("/csv")
def csv_conversions(
    conversion_type: CSV_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "csv":

            csv_controller_object = File_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.csv,
            )
            s3_url = csv_controller_object.convert_file()

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


tsv_router = APIRouter()


@tsv_router.post("/tsv")
def tsv_conversions(
    conversion_type: TSV_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "tsv":

            tsv_controller_object = File_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.tsv,
            )
            s3_url = tsv_controller_object.convert_file()

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


excel_router = APIRouter()


@excel_router.post("/excel")
def excel_conversions(
    conversion_type: EXCEL_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "xlsx":

            excel_controller_object = File_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.xlsx,
            )
            s3_url = excel_controller_object.convert_file()

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


json_router = APIRouter()


@json_router.post("/json")
def json_conversions(
    conversion_type: JSON_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "json":

            json_controller_object = File_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.json,
            )
            s3_url = json_controller_object.convert_file()

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


xml_router = APIRouter()


@xml_router.post("/xml")
def xml_conversions(
    conversion_type: XML_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "xml":

            xml_controller_object = File_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.xml,
            )
            s3_url = xml_controller_object.convert_file()

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


yaml_router = APIRouter()


@yaml_router.post("/yaml")
def yaml_conversions(
    conversion_type: YAML_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "yaml":

            yaml_controller_object = File_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.yaml,
            )
            s3_url = yaml_controller_object.convert_file()

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
