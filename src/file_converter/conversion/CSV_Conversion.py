import pandas as pd

from src.file_converter.utils.File_Conversion_Types import CSV_Conversion_Types


class CSV_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def csv_to_excel_converter(self):
        """
        This function will convert csv to excel format.
        """
        df = pd.read_csv(
            self.input_file_path,
            encoding="utf-8",
            encoding_errors="ignore",
            on_bad_lines="skip",
        )
        df.to_excel(self.output_file_path, encoding="utf-8", index=False)

    def csv_to_html_converter(self):
        """
        This function will convert csv to html format.
        """
        df = pd.read_csv(
            self.input_file_path,
            encoding="utf-8",
            encoding_errors="ignore",
            on_bad_lines="skip",
        )
        df.to_html(self.output_file_path, encoding="utf-8", index=False)

    def csv_to_json_converter(self):
        """
        This function will convert csv to json format.
        """
        df = pd.read_csv(
            self.input_file_path,
            encoding="utf-8",
            encoding_errors="ignore",
            on_bad_lines="skip",
        )
        df.to_json(self.output_file_path, indent=4, orient="records", force_ascii=False)

    def csv_to_tsv_converter(self):
        """
        This function will convert csv to tsv format.
        """
        df = pd.read_csv(
            self.input_file_path,
            sep=",",
            encoding="utf-8",
            encoding_errors="ignore",
            on_bad_lines="skip",
        )
        df.to_csv(self.output_file_path, sep="\t", encoding="utf-8", index=False)

    def csv_to_xml_converter(self):
        """
        This function will convert csv to xml format.
        """
        df = pd.read_csv(
            self.input_file_path,
            encoding="utf-8",
            encoding_errors="ignore",
            on_bad_lines="skip",
        )
        df.to_xml(self.output_file_path, index=False)

    def convert(self):
        try:
            if self.conversion_type == CSV_Conversion_Types.xlsx:
                self.csv_to_excel_converter()
            elif self.conversion_type == CSV_Conversion_Types.html:
                self.csv_to_html_converter()
            elif self.conversion_type == CSV_Conversion_Types.json:
                self.csv_to_json_converter()
            elif self.conversion_type == CSV_Conversion_Types.tsv:
                self.csv_to_tsv_converter()
            elif self.conversion_type == CSV_Conversion_Types.xml:
                self.csv_to_xml_converter()
        except Exception as e:
            raise Exception(
                f"Failed to convert CSV to {self.conversion_type}, Reason: {str(e)}"
            )
