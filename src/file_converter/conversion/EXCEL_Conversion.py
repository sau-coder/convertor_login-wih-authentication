import pandas as pd

from src.file_converter.utils.File_Conversion_Types import EXCEL_Conversion_Types


class EXCEL_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def excel_to_csv_converter(self):
        """
        This function will convert excel to csv format.
        """
        df = pd.read_excel(self.input_file_path)
        df.to_csv(self.output_file_path, index=False)

    def excel_to_json_converter(self):
        """
        This function will convert excel to csv format.
        """
        df = pd.read_excel(self.input_file_path)
        df.to_json(self.output_file_path, indent=4, orient="records")

    def convert(self):
        try:
            if self.conversion_type == EXCEL_Conversion_Types.csv:
                self.excel_to_csv_converter()
            elif self.conversion_type == EXCEL_Conversion_Types.json:
                self.excel_to_json_converter()
        except Exception as e:
            raise Exception(
                f"Failed to convert EXCEL to {self.conversion_type}, Reason: {str(e)}"
            )
