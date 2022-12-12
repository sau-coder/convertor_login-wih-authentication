import base64
from io import BytesIO

import qrcode

from src.document_converter.conversion.Document_Conversion import Document_Conversion
from src.document_converter.utils.Document_Conversion_Types import (
    Conversion_Types,
    PDF_Conversion_Types,
)
from src.utils.remove_static_files import remove_files
from src.utils.s3_utils import S3Events


class Document_Conversion_Controller:
    def __init__(self, file_name, folder_name, conversion_type, type, password=""):
        self.file_name = file_name
        self.folder_name = folder_name
        self.password = password
        self.conversion_type = conversion_type
        self.type = type
        self.input_file = f"{self.folder_name}/{self.file_name}"
        self.output_file = ""
        self.s3_url = ""

    def assign_file_paths(self):
        """
        This function is to pre-process the file names
        """
        file_name = self.file_name.split(".")[0]
        if (
            self.conversion_type == PDF_Conversion_Types.encrypt_pdf
            or self.conversion_type == PDF_Conversion_Types.decrypt_pdf
        ):
            self.output_file = f"{self.folder_name}/{file_name}.pdf"
        else:
            self.output_file = f"{self.folder_name}/{file_name}.{self.conversion_type}"

    def upload_file_function(self):
        """
        This function uploads the file to S3 Storage.
        """
        file_obj = open(self.output_file)
        s3 = S3Events()
        self.s3_url = s3.process_and_upload(
            subdir=f"conversions/{self.type}/",
            file=file_obj,
            file_path=self.output_file,
        )
        file_obj.close()

    def document_converter(self):
        """
        This function will act as a controller for Documents conversion.
        """
        document_conversion_object = Document_Conversion(
            input_file_path=self.input_file,
            output_file_path=self.output_file
            if self.type == Conversion_Types.pdf
            and self.conversion_type != PDF_Conversion_Types.docx
            else self.folder_name,
            password=self.password,
            conversion_type=self.conversion_type,
            type=self.type,
        )
        document_conversion_object.converter()

    def qr_code_generater(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.qr.add_data(self.s3_url)
        self.qr.make(fit=True)

        # Save the QR code image to a BytesIO object
        buffer = BytesIO()
        self.qrimg = self.qr.make_image(fill_color="black", back_color="white")
        self.qrimg.save(buffer, format="PNG")

        # Encode the image in base64
        self.qr_image_data = base64.b64encode(buffer.getvalue()).decode()

    def convert_document(self):

        # assign file paths
        self.assign_file_paths()

        # Document converter
        self.document_converter()

        # upload file to s3 bucket.
        self.upload_file_function()

        # QR code generate for s3 url.
        self.qr_code_generater()

        # remove unecessary folders
        remove_files(folder_name=self.folder_name)

        return (self.s3_url, self.qr_image_data)
