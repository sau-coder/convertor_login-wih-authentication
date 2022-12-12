from src.document_converter.conversion.DOC_Conversion import DOC_Conversion
from src.document_converter.conversion.PDF_Conversion import PDF_Conversion
from src.document_converter.utils.Document_Conversion_Types import Conversion_Types


class Document_Conversion:
    def __init__(
        self, input_file_path, output_file_path, conversion_type, type, password=""
    ):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.password = password
        self.conversion_type = conversion_type
        self.type = type

    def converter(self):
        if self.type == Conversion_Types.pdf:
            pdf_conversion_object = PDF_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                password=self.password,
                conversion_type=self.conversion_type,
            )
            pdf_conversion_object.convert()

        elif self.type == Conversion_Types.docx:
            doc_conversion_Object = DOC_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            doc_conversion_Object.convert()
