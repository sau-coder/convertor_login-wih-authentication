import os

from PIL import Image

from src.image_converter.utils.Image_Conversion_Types import JPG_Conversion_Types


class JPG_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def jpg_to_pdf_converter(self):
        """
        This function will convert jpg to pdf format.
        """
        os.system(f"img2pdf {self.input_file_path} -o {self.output_file_path}")

    def jpg_to_png_converter(self):
        """
        This function will convert jpg to png format.
        """
        Image.open(self.input_file_path).save(self.output_file_path)

    def jpg_to_webp_converter(self):
        """
        This function will convert jpg to webp format.
        """
        Image.open(self.input_file_path).convert("RGB").save(self.output_file_path)

    def jpg_to_images_converter(self):
        """
        This function will convert jpg to bmp, eps, tiff format.
        """
        Image.open(self.input_file_path).convert("RGB").save(self.output_file_path)

    def convert(self):
        try:
            if self.conversion_type == JPG_Conversion_Types.pdf:
                self.jpg_to_pdf_converter()
            elif self.conversion_type == JPG_Conversion_Types.png:
                self.jpg_to_png_converter()
            elif self.conversion_type == JPG_Conversion_Types.webp:
                self.jpg_to_webp_converter()
            else:
                self.jpg_to_images_converter()
        except Exception as e:
            raise Exception(
                f"Failed to convert JPG to {self.conversion_type}, Reason: {str(e)}"
            )
