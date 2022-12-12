import os

import PyPDF2
import tabula
from PyPDF2 import PdfFileReader, PdfFileWriter

from src.config.config import LIBRE_OFFICE
from src.document_converter.utils.Document_Conversion_Types import PDF_Conversion_Types


class PDF_Conversion:
    def __init__(self, input_file_path, output_file_path, password, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.password = password
        self.conversion_type = conversion_type

    def pdf_to_csv_converter(self):
        """
        This function will convert pdf to csv format.
        """
        tabula.convert_into(
            self.input_file_path,
            self.output_file_path,
            output_format="csv",
            pages="all",
        )

    def pdf_to_doc_converter(self):
        """
        This function will convert pdf to doc format.
        """
        os.system(
            f"{LIBRE_OFFICE} --infilter='writer_pdf_import' --convert-to docx {self.input_file_path} --outdir {self.output_file_path}"
        )

    def encrypt_pdf(self):
        """
        This function will encrypt pdf with password.
        """

        pdf_binary = open(self.input_file_path, "rb")
        input_pdf = PyPDF2.PdfFileReader(pdf_binary)
        if input_pdf.isEncrypted:
            raise Exception("File Already Encrypted.")
        pages_no = input_pdf.numPages
        output = PyPDF2.PdfFileWriter()

        for i in range(pages_no):
            input_pdf = PyPDF2.PdfFileReader(pdf_binary)
            output.addPage(input_pdf.getPage(i))
            output.encrypt(self.password)
            with open(self.output_file_path, "wb") as output_stream:
                output.write(output_stream)
        pdf_binary.close()

    def decrypt_pdf(self):
        """
        This function will decrypt pdf passwords.
        """
        # Create a PdfFileWriter object
        out = PdfFileWriter()

        # Open encrypted PDF file with the PdfFileReader
        file = PdfFileReader(self.input_file_path)

        # Check if the opened file is actually Encrypted
        if file.isEncrypted:

            file.decrypt(self.password)

            for idx in range(file.numPages):

                # Get the page at index idx
                page = file.getPage(idx)

                # Add it to the output file
                out.addPage(page)

            with open(self.output_file_path, "wb") as f:
                out.write(f)
        else:
            raise Exception("File Already Decrypted.")

    def pdf_to_png_converter(self):
        # TODO: Need to fix multiple page issues.
        """
        This function will convert pdf to png format.
        """
        os.system(f"pdftoppm {self.input_file_path} {self.output_file_path} -png")

    def pdf_to_jpg_converter(self):
        # TODO: Need to fix multiple page issues.
        """
        This function will convert pdf to jpg format.
        """
        os.system(
            f"pdftoppm -jpeg -r 300 {self.input_file_path} {self.output_file_path}"
        )

    def pdf_to_emf_converter(self):
        """
        This function will convert pdf to emf format.

        This Converter at a Time Only One Page Convert.
        """
        os.system(f"inkscape {self.input_file_path} -M {self.output_file_path}")

    def pdf_to_svg_converter(self):
        # TODO: Need to fix multiple page issues.
        """
        This function will convert pdf to svg format.
        """
        os.system(f"pdf2svg {self.input_file_path} %d{self.output_file_path} all")

    def pdf_to_txt_converter(self):
        """
        This function will convert pdf to txt format.
        """
        myFile = open(self.input_file_path, "rb")
        pdfReader = PyPDF2.PdfFileReader(myFile)
        numOfPages = pdfReader.numPages
        text_ = []

        for i in range(numOfPages):
            page = pdfReader.getPage(i)
            text = page.extractText()
            text_.append(text)

        with open(self.output_file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(text_))
        myFile.close()

    def pdf_to_excel_converter(self):
        """
        This function will convert pdf to excel format.
        """

        tabula.convert_into(
            self.input_file_path,
            self.output_file_path,
            output_format="csv",
            pages="all",
        )

    def convert(self):
        try:
            if self.conversion_type == PDF_Conversion_Types.txt:
                self.pdf_to_txt_converter()
            elif self.conversion_type == PDF_Conversion_Types.xlsx:
                self.pdf_to_excel_converter()
            elif self.conversion_type == PDF_Conversion_Types.csv:
                self.pdf_to_csv_converter()
            elif self.conversion_type == PDF_Conversion_Types.docx:
                self.pdf_to_doc_converter()
            elif self.conversion_type == PDF_Conversion_Types.encrypt_pdf:
                self.encrypt_pdf()
            elif self.conversion_type == PDF_Conversion_Types.decrypt_pdf:
                self.decrypt_pdf()
            elif self.conversion_type == PDF_Conversion_Types.png:
                self.pdf_to_png_converter()
            elif self.conversion_type == PDF_Conversion_Types.jpg:
                self.pdf_to_jpg_converter()
            elif self.conversion_type == PDF_Conversion_Types.emf:
                self.pdf_to_emf_converter()
            elif self.conversion_type == PDF_Conversion_Types.svg:
                self.pdf_to_svg_converter()

        except Exception as e:
            raise Exception(
                f"Failed to convert PDF to {self.conversion_type}, Reason: {str(e)}"
            )
