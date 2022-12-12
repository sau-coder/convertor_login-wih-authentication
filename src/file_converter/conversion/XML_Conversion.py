import pandas_read_xml as pdx

from src.file_converter.utils.File_Conversion_Types import XML_Conversion_Types


class XML_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def xml_to_csv_converter(self):
        """
        This function will convert xml to csv format.
        """
        df = pdx.read_xml(self.input_file_path, encoding="utf-8")
        df.to_csv(self.output_file_path, index=False, encoding="utf-8")

    def xml_to_excel_converter(self):
        """
        This function will convert xml to excel format.
        """
        df = pdx.read_xml(self.input_file_path, encoding="utf-8")
        df.to_excel(self.output_file_path, index=False, encoding="utf-8")

    def xml_to_json_converter(self):
        """
        This function will convert xml to json format.
        """
        df = pdx.read_xml(self.input_file_path, encoding="utf-8")
        df.to_json(self.output_file_path, indent=4, orient="records")

    def convert(self):
        try:
            if self.conversion_type == XML_Conversion_Types.csv:
                self.xml_to_csv_converter()
            elif self.conversion_type == XML_Conversion_Types.xlsx:
                self.xml_to_excel_converter()
            elif self.conversion_type == XML_Conversion_Types.json:
                self.xml_to_json_converter()
        except Exception as e:
            raise Exception(
                f"Failed to convert XML to {self.conversion_type}, Reason: {str(e)}"
            )
