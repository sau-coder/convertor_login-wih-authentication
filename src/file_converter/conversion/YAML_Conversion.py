import json

import ruamel.yaml

from src.file_converter.utils.File_Conversion_Types import YAML_Conversion_Types


class YAML_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def yaml_to_json_converter(self):
        """
        This function will convert yaml to json format.
        """
        yaml = ruamel.yaml.YAML(typ="safe")
        with open(self.input_file_path) as file:
            data = yaml.load(file)
        with open(self.output_file_path, "w") as outfile:
            json.dump(data, outfile, indent=4)

    def convert(self):
        try:
            if self.conversion_type == YAML_Conversion_Types.json:
                self.yaml_to_json_converter()

        except Exception as e:
            raise Exception(
                f"Failed to convert YAML to {self.conversion_type}, Reason: {str(e)}"
            )
