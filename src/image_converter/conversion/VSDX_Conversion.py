import jpype
from asposediagram.api import Diagram, SaveFileFormat

from src.image_converter.utils.Image_Conversion_Types import VSDX_Conversion_Types

# Start the JVM machine
if not jpype.isJVMStarted():
    jpype.startJVM()


class VSDX_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def vsdx_to_pdf_converter(self):
        """
        This function will convert vsdx to pdf format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PDF)

    def vsdx_to_png_converter(self):
        """
        This function will convert vsdx to png format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_tiff_converter(self):
        """
        This function will convert vsdx to tiff format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_jpg_converter(self):
        """
        This function will convert vsdx to jpg format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.JPEG)

    def vsdx_to_bmp_converter(self):
        """
        This function will convert vsdx to bmp format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_emf_converter(self):
        """
        This function will convert vsdx to emf format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_docx_converter(self):
        """
        This function will convert vsdx to docx format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_pptx_converter(self):
        """
        This function will convert vsdx to pptx format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_eps_converter(self):
        """
        This function will convert vsdx to eps format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_webp_converter(self):
        """
        This function will convert vsdx to webp format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_text_converter(self):
        """
        This function will convert vsdx to text format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_svg_converter(self):
        """
        This function will convert vsdx to svg format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.SVG)

    def vsdx_to_heic_converter(self):
        """
        This function will convert vsdx to heic format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_psd_converter(self):
        """
        This function will convert vsdx to psd format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsdx_to_vsd_converter(self):
        """
        This function will convert vsdx to vsd format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def convert(self):
        try:
            if self.conversion_type == VSDX_Conversion_Types.pdf:
                self.vsdx_to_pdf_converter()
            elif self.conversion_type == VSDX_Conversion_Types.png:
                self.vsdx_to_png_converter()
            elif self.conversion_type == VSDX_Conversion_Types.tiff:
                self.vsdx_to_tiff_converter()
            elif self.conversion_type == VSDX_Conversion_Types.jpg:
                self.vsdx_to_jpg_converter()
            elif self.conversion_type == VSDX_Conversion_Types.bmp:
                self.vsdx_to_bmp_converter()
            elif self.conversion_type == VSDX_Conversion_Types.emf:
                self.vsdx_to_emf_converter()
            elif self.conversion_type == VSDX_Conversion_Types.docx:
                self.vsdx_to_docx_converter()
            elif self.conversion_type == VSDX_Conversion_Types.pptx:
                self.vsdx_to_pptx_converter()
            elif self.conversion_type == VSDX_Conversion_Types.eps:
                self.vsdx_to_eps_converter()
            elif self.conversion_type == VSDX_Conversion_Types.webp:
                self.vsdx_to_webp_converter()
            elif self.conversion_type == VSDX_Conversion_Types.text:
                self.vsdx_to_text_converter()
            elif self.conversion_type == VSDX_Conversion_Types.svg:
                self.vsdx_to_svg_converter()
            elif self.conversion_type == VSDX_Conversion_Types.heic:
                self.vsdx_to_heic_converter()
            elif self.conversion_type == VSDX_Conversion_Types.psd:
                self.vsdx_to_psd_converter()
            elif self.conversion_type == VSDX_Conversion_Types.vsd:
                self.vsdx_to_vsd_converter()
        except Exception as e:
            raise Exception(
                f"Failed to convert VSDX to {self.conversion_type}, Reason: {str(e)}"
            )
