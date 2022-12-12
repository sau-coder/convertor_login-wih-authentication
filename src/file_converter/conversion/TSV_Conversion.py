import pandas as pd

from src.file_converter.utils.File_Conversion_Types import TSV_Conversion_Types


class TSV_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def tsv_to_csv_converter(self):
        """
        This function will convert tsv to csv format.
        """
        df = pd.read_table(
            self.input_file_path,
            sep="\t",
            encoding="utf-8",
            encoding_errors="ignore",
            on_bad_lines="skip",
        )
        df.to_csv(self.output_file_path, encoding="utf-8", index=False)

    def convert(self):
        try:
            if self.conversion_type == TSV_Conversion_Types.csv:
                self.tsv_to_csv_converter()

        except Exception as e:
            raise Exception(
                f"Failed to convert TSV to {self.conversion_type}, Reason: {str(e)}"
            )
