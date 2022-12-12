import jpype

# need to start the JVM
jpype.startJVM(jpype.getDefaultJVMPath())

from asposediagram.api import Diagram, SaveFileFormat  # noqa: E402

from src.image_converter.utils.Image_Conversion_Types import (  # noqa: E402
    VSD_Conversion_Types,
)


class VSD_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def vsd_to_pdf_converter(self):
        """
        This function will convert vsd to pdf format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PDF)

    def vsd_to_png_converter(self):
        """
        This function will convert vsd to png format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_tiff_converter(self):
        """
        This function will convert vsd to tiff format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_jpg_converter(self):
        """
        This function will convert vsd to jpg format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.JPEG)

    def vsd_to_bmp_converter(self):
        """
        This function will convert vsd to bmp format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_emf_converter(self):
        """
        This function will convert vsd to emf format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_docx_converter(self):
        """
        This function will convert vsd to docx format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_pptx_converter(self):
        """
        This function will convert vsd to pptx format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_eps_converter(self):
        """
        This function will convert vsd to eps format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_webp_converter(self):
        """
        This function will convert vsd to webp format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_text_converter(self):
        """
        This function will convert vsd to text format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_svg_converter(self):
        """
        This function will convert vsd to svg format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.SVG)

    def vsd_to_heic_converter(self):
        """
        This function will convert vsd to heic format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_psd_converter(self):
        """
        This function will convert vsd to psd format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def vsd_to_vsdx_converter(self):
        """
        This function will convert vsd to vsdx format.
        """
        diagram = Diagram(self.input_file_path)
        diagram.save(self.output_file_path, SaveFileFormat.PNG)

    def convert(self):
        try:
            if self.conversion_type == VSD_Conversion_Types.pdf:
                self.vsd_to_pdf_converter()
            elif self.conversion_type == VSD_Conversion_Types.png:
                self.vsd_to_png_converter()
            elif self.conversion_type == VSD_Conversion_Types.tiff:
                self.vsd_to_tiff_converter()
            elif self.conversion_type == VSD_Conversion_Types.jpg:
                self.vsd_to_jpg_converter()
            elif self.conversion_type == VSD_Conversion_Types.bmp:
                self.vsd_to_bmp_converter()
            elif self.conversion_type == VSD_Conversion_Types.emf:
                self.vsd_to_emf_converter()
            elif self.conversion_type == VSD_Conversion_Types.docx:
                self.vsd_to_docx_converter()
            elif self.conversion_type == VSD_Conversion_Types.pptx:
                self.vsd_to_pptx_converter()
            elif self.conversion_type == VSD_Conversion_Types.eps:
                self.vsd_to_eps_converter()
            elif self.conversion_type == VSD_Conversion_Types.webp:
                self.vsd_to_webp_converter()
            elif self.conversion_type == VSD_Conversion_Types.text:
                self.vsd_to_text_converter()
            elif self.conversion_type == VSD_Conversion_Types.svg:
                self.vsd_to_svg_converter()
            elif self.conversion_type == VSD_Conversion_Types.heic:
                self.vsd_to_heic_converter()
            elif self.conversion_type == VSD_Conversion_Types.psd:
                self.vsd_to_psd_converter()
            elif self.conversion_type == VSD_Conversion_Types.vsdx:
                self.vsd_to_vsdx_converter()

        except Exception as e:
            raise Exception(
                f"Failed to convert VSD to {self.conversion_type}, Reason: {str(e)}"
            )
