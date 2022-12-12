from typing import Optional

from fastapi import APIRouter, File, Form, UploadFile, status
from fastapi.responses import JSONResponse

from src.document_converter.controller.Document_Conversion_Controller import (
    Document_Conversion_Controller,
)
from src.document_converter.utils.Document_Conversion_Types import (
    Conversion_Types,
    DOC_Conversion_Types,
    PDF_Conversion_Types,
)
from src.utils.extension_checker import extension_checker
from src.utils.file_download import save_file
from src.utils.remove_static_files import remove_files

pdf_router = APIRouter()


@pdf_router.post("/pdf")
def pdf_conversions(
    conversion_type: PDF_Conversion_Types = Form(None),
    file: UploadFile = File(None),
    password: Optional[str] = Form(None),
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "pdf":

            pdf_controller_object = Document_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                password=password,
                conversion_type=conversion_type,
                type=Conversion_Types.pdf,
            )
            s3_url = pdf_controller_object.convert_document()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Document Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static documents if error occurs
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
        # Remove static documents if error occurs
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


doc_router = APIRouter()


@doc_router.post("/docx")
def doc_conversions(
    conversion_type: DOC_Conversion_Types = Form(None), file: UploadFile = File(None)
):
    try:
        file_name, folder_name = save_file(file=file)
        doc_result = extension_checker(file_name)

        if doc_result == "docx":

            doc_controller_object = Document_Conversion_Controller(
                file_name=file_name,
                folder_name=folder_name,
                conversion_type=conversion_type,
                type=Conversion_Types.docx,
            )
            s3_url = doc_controller_object.convert_document()

            # Saving the response
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Document Converted Successfully",
                    "error": None,
                    "data": {"url": s3_url},
                }
            )

        else:
            # Remove static documents if error occurs
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
        # Remove static documents if error occurs
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
