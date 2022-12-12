from src.video_converter.conversion.AVI_Conversion import AVI_Conversion
from src.video_converter.conversion.MKV_Conversion import MKV_Conversion
from src.video_converter.conversion.MOV_Conversion import MOV_Conversion
from src.video_converter.conversion.MP4_Conversion import MP4_Conversion
from src.video_converter.utils.Video_Conversion_Types import Conversion_Types


class Video_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type, type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type
        self.type = type

    def converter(self):
        if self.type == Conversion_Types.mp4:
            mp4_conversion_object = MP4_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            mp4_conversion_object.convert()

        elif self.type == Conversion_Types.mov:
            mov_conversion_object = MOV_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            mov_conversion_object.convert()

        elif self.type == Conversion_Types.mkv:
            mkv_conversion_object = MKV_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            mkv_conversion_object.convert()

        elif self.type == Conversion_Types.avi:
            avi_conversion_object = AVI_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            avi_conversion_object.convert()
