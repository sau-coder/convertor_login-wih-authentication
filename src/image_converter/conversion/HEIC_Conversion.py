import pillow_heif
from PIL import Image

from src.image_converter.utils.Image_Conversion_Types import HEIC_Conversion_Types


class HEIC_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def heic_to_png_converter(self):
        """
        This function will convert heic to png format.
        """
        heif_file = pillow_heif.read_heif(self.input_file_path)
        Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw").save(
            self.output_file_path
        )

    def heic_to_bmp_converter(self):
        """
        This function will convert heic to bmp format.
        """
        heif_file = pillow_heif.read_heif(self.input_file_path)
        Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw").save(
            self.output_file_path
        )

    def heic_to_eps_converter(self):
        """
        This function will convert heic to eps format.
        """
        heif_file = pillow_heif.read_heif(self.input_file_path)
        Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw").save(
            self.output_file_path
        )

    def heic_to_jpg_converter(self):
        """
        This function will convert heic to jpg format.
        """
        heif_file = pillow_heif.read_heif(self.input_file_path)
        Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw").save(
            self.output_file_path
        )

    def heic_to_pdf_converter(self):
        """
        This function will convert heic to pdf format.
        """
        heif_file = pillow_heif.read_heif(self.input_file_path)
        Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw").save(
            self.output_file_path
        )

    def heic_to_tiff_converter(self):
        """
        This function will convert heic to tiff format.
        """
        heif_file = pillow_heif.read_heif(self.input_file_path)
        Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw").save(
            self.output_file_path
        )

    def heic_to_webp_converter(self):
        """
        This function will convert heic to webp format.
        """
        heif_file = pillow_heif.read_heif(self.input_file_path)
        Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw").save(
            self.output_file_path
        )

    def convert(self):
        try:
            if self.conversion_type == HEIC_Conversion_Types.png:
                self.heic_to_png_converter()
            elif self.conversion_type == HEIC_Conversion_Types.bmp:
                self.heic_to_bmp_converter()
            elif self.conversion_type == HEIC_Conversion_Types.eps:
                self.heic_to_eps_converter()
            elif self.conversion_type == HEIC_Conversion_Types.jpg:
                self.heic_to_jpg_converter()
            elif self.conversion_type == HEIC_Conversion_Types.pdf:
                self.heic_to_pdf_converter()
            elif self.conversion_type == HEIC_Conversion_Types.tiff:
                self.heic_to_tiff_converter()
            elif self.conversion_type == HEIC_Conversion_Types.webp:
                self.heic_to_webp_converter()

        except Exception as e:
            raise Exception(
                f"Failed to convert HEIC to {self.conversion_type}, Reason: {str(e)}"
            )
