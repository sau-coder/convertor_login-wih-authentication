from src.image_converter.conversion.BMP_Conversion import BMP_Conversion
from src.image_converter.conversion.HEIC_Conversion import HEIC_Conversion
from src.image_converter.conversion.JPG_Conversion import JPG_Conversion
from src.image_converter.conversion.PNG_Conversion import PNG_Conversion
from src.image_converter.conversion.PSD_Conversion import PSD_Conversion
from src.image_converter.conversion.SVG_Conversion import SVG_Conversion
from src.image_converter.conversion.TIFF_Conversion import TIFF_Conversion
from src.image_converter.conversion.VSD_Conversion import VSD_Conversion
from src.image_converter.conversion.VSDX_Conversion import VSDX_Conversion
from src.image_converter.conversion.WEBP_Conversion import WEBP_Conversion
from src.image_converter.utils.Image_Conversion_Types import Conversion_Types


class Image_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type, type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type
        self.type = type

    def converter(self):
        if self.type == Conversion_Types.jpg:
            jpg_conversion_object = JPG_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            jpg_conversion_object.convert()

        elif self.type == Conversion_Types.png:
            png_conversion_object = PNG_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            png_conversion_object.convert()

        elif self.type == Conversion_Types.webp:
            webp_conversion_object = WEBP_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            webp_conversion_object.convert()

        elif self.type == Conversion_Types.tiff:
            tiff_conversion_object = TIFF_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            tiff_conversion_object.convert()

        elif self.type == Conversion_Types.psd:
            psd_conversion_object = PSD_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            psd_conversion_object.convert()

        elif self.type == Conversion_Types.svg:
            svg_conversion_object = SVG_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            svg_conversion_object.convert()

        elif self.type == Conversion_Types.vsd:
            vsd_conversion_object = VSD_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            vsd_conversion_object.convert()

        elif self.type == Conversion_Types.vsdx:
            vsdx_conversion_object = VSDX_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            vsdx_conversion_object.convert()

        elif self.type == Conversion_Types.bmp:
            bmp_conversion_object = BMP_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            bmp_conversion_object.convert()

        elif self.type == Conversion_Types.heic:
            heic_conversion_object = HEIC_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            heic_conversion_object.convert()
