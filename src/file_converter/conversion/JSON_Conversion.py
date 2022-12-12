import json

import pandas as pd
import yaml

from src.file_converter.utils.File_Conversion_Types import JSON_Conversion_Types


class JSON_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def json_to_csv_converter(self):
        """
        This function will convert json to csv format.
        """
        df = pd.read_json(
            self.input_file_path, encoding="utf-8", encoding_errors="ignore"
        )
        df.to_csv(self.output_file_path, index=False, encoding="utf-8")

    def json_to_excel_converter(self):
        """
        This function will convert json to excel format.
        """
        df = pd.read_json(
            self.input_file_path, encoding="utf-8", encoding_errors="ignore"
        )
        df.to_excel(self.output_file_path, index=False)

    def json_to_xml_converter(self):
        """
        This function will convert json to xml format.
        """
        df = pd.read_json(
            self.input_file_path, encoding="utf-8", encoding_errors="ignore"
        )
        df.to_xml(self.output_file_path, index=False)

    def json_to_yaml_converter(self):
        """
        This function will convert json to yaml format.
        """
        with open(self.input_file_path, encoding="utf-8") as file:
            data = json.loads(file.read())
        with open(self.output_file_path, "w", encoding="utf-8") as outfile:
            yaml.dump(data, outfile, encoding="utf-8", allow_unicode=False)

    def convert(self):
        try:
            if self.conversion_type == JSON_Conversion_Types.csv:
                self.json_to_csv_converter()
            elif self.conversion_type == JSON_Conversion_Types.xlsx:
                self.json_to_excel_converter()
            elif self.conversion_type == JSON_Conversion_Types.xml:
                self.json_to_xml_converter()
            elif self.conversion_type == JSON_Conversion_Types.yaml:
                self.json_to_yaml_converter()
        except Exception as e:
            raise Exception(
                f"Failed to convert JSON to {self.conversion_type}, Reason: {str(e)}"
            )
