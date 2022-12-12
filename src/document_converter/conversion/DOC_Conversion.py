import os

from src.config.config import LIBRE_OFFICE
from src.document_converter.utils.Document_Conversion_Types import DOC_Conversion_Types


class DOC_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def doc_to_docx_converter(self):
        """
        This function will convert doc to docx format.
        """
        os.system(
            f"{LIBRE_OFFICE} --convert-to docx {self.input_file_path} --outdir {self.output_file_path}"
        )

    def docx_to_doc_converter(self):
        """
        This function will convert docx to doc format.
        """
        os.system(
            f"{LIBRE_OFFICE} --convert-to doc {self.input_file_path} --outdir {self.output_file_path}"
        )

    def doc_to_pdf_converter(self):
        """
        This function will convert docx to pdf format.
        """
        os.system(
            f"{LIBRE_OFFICE} --convert-to pdf {self.input_file_path} --outdir {self.output_file_path}"
        )

    def doc_to_txt_converter(self):
        """
        This function will convert docx to txt format.
        """
        os.system(
            f"{LIBRE_OFFICE} --convert-to txt {self.input_file_path} --outdir {self.output_file_path}"
        )

    def convert(self):
        try:
            if self.conversion_type == DOC_Conversion_Types.docx:
                self.doc_to_docx_converter()
            elif self.conversion_type == DOC_Conversion_Types.doc:
                self.docx_to_doc_converter()
            elif self.conversion_type == DOC_Conversion_Types.pdf:
                self.doc_to_pdf_converter()
            elif self.conversion_type == DOC_Conversion_Types.txt:
                self.doc_to_txt_converter()

        except Exception as e:
            raise Exception(
                f"Failed to convert DOC to {self.conversion_type}, Reason: {str(e)}"
            )
