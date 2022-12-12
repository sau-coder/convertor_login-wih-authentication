import os

from src.video_converter.utils.Video_Conversion_Types import MKV_Conversion_Types


class MKV_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def mkv_to_gif_conversion(self):
        """
        This function will convert mkv to gif format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -r 10 -loop 0 -to 4 {self.output_file_path}"
        )

    def mkv_to_mp3_conversion(self):
        """
        This function will convert mkv to mp3 format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mkv_to_mp4_conversion(self):
        """
        This function will convert mkv to mp4 format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -filter:v scale=360:-1 -acodec copy {self.output_file_path}"
        )

    def mkv_to_mov_conversion(self):
        """
        This function will convert mkv to mov format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -filter:v scale=360:-1 -acodec copy  {self.output_file_path}"
        )

    def mkv_to_ogg_conversion(self):
        """
        This function will convert mkv to ogg format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mkv_to_wav_conversion(self):
        """
        This function will convert mkv to wav format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mkv_to_aac_conversion(self):
        """
        This function will convert mkv to wav format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mkv_to_avi_conversion(self):
        """
        This function will convert mkv to avi format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def convert(self):
        try:
            if self.conversion_type == MKV_Conversion_Types.gif:
                self.mkv_to_gif_conversion()
            elif self.conversion_type == MKV_Conversion_Types.mp3:
                self.mkv_to_mp3_conversion()
            elif self.conversion_type == MKV_Conversion_Types.mp4:
                self.mkv_to_mp4_conversion()
            elif self.conversion_type == MKV_Conversion_Types.wav:
                self.mkv_to_wav_conversion()
            elif self.conversion_type == MKV_Conversion_Types.aac:
                self.mkv_to_wav_conversion()
            elif self.conversion_type == MKV_Conversion_Types.ogg:
                self.mkv_to_ogg_conversion()
            elif self.conversion_type == MKV_Conversion_Types.avi:
                self.mkv_to_avi_conversion()
            elif self.conversion_type == MKV_Conversion_Types.mov:
                self.mkv_to_mov_conversion()
        except Exception as e:
            raise Exception(
                f"Failed to convert MKV to {self.conversion_type}, Reason: {str(e)}"
            )
