from PIL import Image


class PNG_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def png_to_images_converter(self):
        """
        This function will convert png to jpg, pdf, bmp, eps, tiff, webp format.
        """
        Image.open(self.input_file_path).convert("RGB").save(self.output_file_path)

    def convert(self):
        try:
            self.png_to_images_converter()
        except Exception as e:
            raise Exception(
                f"Failed to convert PNG to {self.conversion_type}, Reason: {str(e)}"
            )
