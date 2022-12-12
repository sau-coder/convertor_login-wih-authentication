import base64
from io import BytesIO

import qrcode

from src.audio_converter.conversion.Audio_Conversion import Audio_Conversion
from src.utils.remove_static_files import remove_files
from src.utils.s3_utils import S3Events


class Audio_Conversion_Controller:
    def __init__(self, file_name, folder_name, conversion_type, type):
        self.file_name = file_name
        self.folder_name = folder_name
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

    def file_converter(self):
        """
        This function will act as a controller for audio conversion.
        """
        audio_conversion_object = Audio_Conversion(
            input_file_path=self.input_file,
            output_file_path=self.output_file,
            conversion_type=self.conversion_type,
            type=self.type,
        )
        audio_conversion_object.converter()

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

    def convert_file(self):

        # assign file paths
        self.assign_file_paths()

        # file converter
        self.file_converter()

        # upload file to s3 bucket.
        self.upload_file_function()

        # QR code generate for s3 url.
        self.qr_code_generater()

        # remove unecessary folders
        remove_files(folder_name=self.folder_name)

        return (self.s3_url, self.qr_image_data)
