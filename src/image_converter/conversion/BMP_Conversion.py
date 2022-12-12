import aspose.words as aw

from src.image_converter.utils.Image_Conversion_Types import BMP_Conversion_Types


class BMP_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def bmp_to_jpg_converter(self):
        """
        This function will convert bmp to jpg format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def bmp_to_png_converter(self):
        """
        This function will convert bmp to png format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def bmp_to_tiff_converter(self):
        """
        This function will convert bmp to tiff format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def bmp_to_pdf_converter(self):
        """
        This function will convert bmp to pdf format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def bmp_to_emf_converter(self):
        """
        This function will convert bmp to emf format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def bmp_to_svg_converter(self):
        """
        This function will convert bmp to svg format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def bmp_to_docx_converter(self):
        """
        This function will convert bmp to docx format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def convert(self):
        try:
            if self.conversion_type == BMP_Conversion_Types.jpg:
                self.bmp_to_jpg_converter()
            elif self.conversion_type == BMP_Conversion_Types.png:
                self.bmp_to_png_converter()
            elif self.conversion_type == BMP_Conversion_Types.tiff:
                self.bmp_to_tiff_converter()
            elif self.conversion_type == BMP_Conversion_Types.pdf:
                self.bmp_to_pdf_converter()
            elif self.conversion_type == BMP_Conversion_Types.emf:
                self.bmp_to_emf_converter()
            elif self.conversion_type == BMP_Conversion_Types.svg:
                self.bmp_to_svg_converter()
            elif self.conversion_type == BMP_Conversion_Types.docx:
                self.bmp_to_docx_converter()

        except Exception as e:
            raise Exception(
                f"Failed to convert BMP to {self.conversion_type}, Reason: {str(e)}"
            )
