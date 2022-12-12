from src.file_converter.conversion.CSV_Conversion import CSV_Conversion
from src.file_converter.conversion.EXCEL_Conversion import EXCEL_Conversion
from src.file_converter.conversion.JSON_Conversion import JSON_Conversion
from src.file_converter.conversion.TSV_Conversion import TSV_Conversion
from src.file_converter.conversion.XML_Conversion import XML_Conversion
from src.file_converter.conversion.YAML_Conversion import YAML_Conversion
from src.file_converter.utils.File_Conversion_Types import Conversion_Types


class File_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type, type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type
        self.type = type

    def converter(self):
        if self.type == Conversion_Types.csv:
            csv_conversion_object = CSV_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            csv_conversion_object.convert()
        elif self.type == Conversion_Types.tsv:
            tsv_conversion_object = TSV_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            tsv_conversion_object.convert()
        elif self.type == Conversion_Types.xlsx:
            excel_conversion_object = EXCEL_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            excel_conversion_object.convert()
        elif self.type == Conversion_Types.json:
            json_conversion_object = JSON_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            json_conversion_object.convert()
        elif self.type == Conversion_Types.xml:
            xml_conversion_object = XML_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            xml_conversion_object.convert()
        elif self.type == Conversion_Types.yaml:
            yaml_conversion_object = YAML_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            yaml_conversion_object.convert()
