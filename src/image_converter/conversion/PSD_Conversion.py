from psd_tools import PSDImage

from src.image_converter.utils.Image_Conversion_Types import PSD_Conversion_Types


class PSD_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def psd_to_jpg_converter(self):
        """
        This function will convert psd to jpg format.
        """
        PSDImage.open(self.input_file_path).composite().save(self.output_file_path)

    def psd_to_png_converter(self):
        """
        This function will convert psd to png format.
        """
        PSDImage.open(self.input_file_path).composite().save(self.output_file_path)

    def psd_to_bmp_converter(self):
        """
        This function will convert psd to bmp format.
        """
        PSDImage.open(self.input_file_path).composite().save(self.output_file_path)

    def psd_to_eps_converter(self):
        """
        This function will convert psd to eps format.
        """
        PSDImage.open(self.input_file_path).composite().save(self.output_file_path)

    def psd_to_pdf_converter(self):
        """
        This function will convert psd to pdf format.
        """
        PSDImage.open(self.input_file_path).composite().save(self.output_file_path)

    def psd_to_tiff_converter(self):
        """
        This function will convert psd to tiff format.
        """
        PSDImage.open(self.input_file_path).composite().save(self.output_file_path)

    def psd_to_webp_converter(self):
        """
        This function will convert psd to webp format.
        """
        PSDImage.open(self.input_file_path).composite().save(self.output_file_path)

    def convert(self):
        try:
            if self.conversion_type == PSD_Conversion_Types.jpg:
                self.psd_to_jpg_converter()
            elif self.conversion_type == PSD_Conversion_Types.png:
                self.psd_to_png_converter()
            elif self.conversion_type == PSD_Conversion_Types.bmp:
                self.psd_to_bmp_converter()
            elif self.conversion_type == PSD_Conversion_Types.eps:
                self.psd_to_eps_converter()
            elif self.conversion_type == PSD_Conversion_Types.pdf:
                self.psd_to_pdf_converter()
            elif self.conversion_type == PSD_Conversion_Types.tiff:
                self.psd_to_tiff_converter()
            elif self.conversion_type == PSD_Conversion_Types.webp:
                self.psd_to_webp_converter()

        except Exception as e:
            raise Exception(
                f"Failed to convert PSD to {self.conversion_type}, Reason: {str(e)}"
            )
