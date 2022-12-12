import aspose.words as aw


class TIFF_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def tiff_to_file_converter(self):
        """
        This is a common function to convert tiff to png, jpg, svg, docx, text, bmp and pdf formats.
        """
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.insert_image(self.input_file_path)
        doc.save(self.output_file_path)

    def convert(self):
        try:
            self.tiff_to_file_converter()
        except Exception as e:
            raise Exception(
                f"Failed to convert TIFF to {self.conversion_type}, Reason: {str(e)}"
            )
