import os

from src.video_converter.utils.Video_Conversion_Types import AVI_Conversion_Types


class AVI_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def avi_to_gif_conversion(self):
        """
        This function will convert avi to gif format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -r 10 -loop 0 -to 4 {self.output_file_path}"
        )

    def avi_to_mp3_conversion(self):
        """
        This function will convert avi to mp3 format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def avi_to_mp4_conversion(self):
        """
        This function will convert avi to mp4 format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -filter:v scale=360:-1  {self.output_file_path}"
        )

    def avi_to_ogg_conversion(self):
        """
        This function will convert avi to ogg format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def avi_to_wav_conversion(self):
        """
        This function will convert avi to wav format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def avi_to_mkv_conversion(self):
        """
        This function will convert avi to mkv format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -filter:v scale=360:-1 -acodec copy {self.output_file_path}"
        )

    def avi_to_mov_conversion(self):
        """
        This function will convert avi to mov format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -filter:v scale=360:-1 -acodec copy  {self.output_file_path}"
        )

    def avi_to_aac_conversion(self):
        """
        This function will convert avi to aac format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def convert(self):
        try:
            if self.conversion_type == AVI_Conversion_Types.gif:
                self.avi_to_gif_conversion()
            elif self.conversion_type == AVI_Conversion_Types.mp3:
                self.avi_to_mp3_conversion()
            elif self.conversion_type == AVI_Conversion_Types.mp4:
                self.avi_to_mp4_conversion()
            elif self.conversion_type == AVI_Conversion_Types.wav:
                self.avi_to_wav_conversion()
            elif self.conversion_type == AVI_Conversion_Types.ogg:
                self.avi_to_ogg_conversion()
            elif self.conversion_type == AVI_Conversion_Types.mkv:
                self.avi_to_mkv_conversion()
            elif self.conversion_type == AVI_Conversion_Types.mov:
                self.avi_to_mov_conversion()
            elif self.conversion_type == AVI_Conversion_Types.aac:
                self.avi_to_aac_conversion()
        except Exception as e:
            raise Exception(
                f"Failed to convert AVI to {self.conversion_type}, Reason: {str(e)}"
            )
