from PIL import Image


class WEBP_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def webp_to_images_converter(self):
        """
        This function will convert webp to jpg, PNG, BMP, EPS, PDF, TIFF format.
        """
        Image.open(self.input_file_path).convert("RGB").save(self.output_file_path)

    def convert(self):
        try:
            self.webp_to_images_converter()
        except Exception as e:
            raise Exception(
                f"Failed to convert WEBP to {self.conversion_type}, Reason: {str(e)}"
            )
