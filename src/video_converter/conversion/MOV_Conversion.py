import os

from src.video_converter.utils.Video_Conversion_Types import MOV_Conversion_Types


class MOV_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def mov_to_gif_conversion(self):
        """
        This function will convert mov to gif format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -r 10 -loop 0 -to 4 {self.output_file_path}"
        )

    def mov_to_mp3_conversion(self):
        """
        This function will convert mov to mp3 format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mov_to_mp4_conversion(self):
        """
        This function will convert mov to mp4 format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -filter:v scale=360:-1 -acodec copy {self.output_file_path}"
        )

    def mov_to_mkv_conversion(self):
        """
        This function will convert mov to mkv format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -filter:v scale=360:-1 -acodec copy  {self.output_file_path}"
        )

    def mov_to_ogg_conversion(self):
        """
        This function will convert mov to ogg format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mov_to_wav_conversion(self):
        """
        This function will convert mov to wav format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mov_to_aac_conversion(self):
        """
        This function will convert mov to wav format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mov_to_avi_conversion(self):
        """
        This function will convert mov to avi format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def convert(self):
        try:
            if self.conversion_type == MOV_Conversion_Types.gif:
                self.mov_to_gif_conversion()
            elif self.conversion_type == MOV_Conversion_Types.mp3:
                self.mov_to_mp3_conversion()
            elif self.conversion_type == MOV_Conversion_Types.mp4:
                self.mov_to_mp4_conversion()
            elif self.conversion_type == MOV_Conversion_Types.wav:
                self.mov_to_wav_conversion()
            elif self.conversion_type == MOV_Conversion_Types.aac:
                self.mov_to_wav_conversion()
            elif self.conversion_type == MOV_Conversion_Types.ogg:
                self.mov_to_ogg_conversion()
            elif self.conversion_type == MOV_Conversion_Types.avi:
                self.mov_to_avi_conversion()
            elif self.conversion_type == MOV_Conversion_Types.mkv:
                self.mov_to_mkv_conversion()
        except Exception as e:
            raise Exception(
                f"Failed to convert MKV to {self.conversion_type}, Reason: {str(e)}"
            )
