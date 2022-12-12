import aspose.words as aw

from src.image_converter.utils.Image_Conversion_Types import SVG_Conversion_Types


class SVG_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def svg_to_png_converter(self):
        """
        This function will convert svg to png format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def svg_to_jpg_converter(self):
        """
        This function will convert svg to jpg format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def svg_to_tiff_converter(self):
        """
        This function will convert svg to tiff format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def svg_to_docx_converter(self):
        """
        This function will convert svg to docx format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def svg_to_bmp_converter(self):
        """
        This function will convert svg to bmp format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def svg_to_emf_converter(self):
        """
        This function will convert svg to emf  format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def svg_to_text_converter(self):
        """
        This function will convert svg to text format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def svg_to_pdf_converter(self):
        """
        This function will convert svg to pdf format.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def convert(self):
        try:
            if self.conversion_type == SVG_Conversion_Types.png:
                self.svg_to_png_converter()
            elif self.conversion_type == SVG_Conversion_Types.jpg:
                self.svg_to_jpg_converter()
            elif self.conversion_type == SVG_Conversion_Types.tiff:
                self.svg_to_tiff_converter()
            elif self.conversion_type == SVG_Conversion_Types.docx:
                self.svg_to_docx_converter()
            elif self.conversion_type == SVG_Conversion_Types.bmp:
                self.svg_to_bmp_converter()
            elif self.conversion_type == SVG_Conversion_Types.emf:
                self.svg_to_emf_converter()
            elif self.conversion_type == SVG_Conversion_Types.text:
                self.svg_to_text_converter()
            elif self.conversion_type == SVG_Conversion_Types.pdf:
                self.svg_to_pdf_converter()

        except Exception as e:
            raise Exception(
                f"Failed to convert SVG to {self.conversion_type}, Reason: {str(e)}"
            )
