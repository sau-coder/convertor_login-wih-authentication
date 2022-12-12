import os

from src.video_converter.utils.Video_Conversion_Types import MP4_Conversion_Types


class MP4_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def mp4_to_gif_conversion(self):
        """
        This function will convert avi to gif format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -r 5 -loop 0 -to 4 {self.output_file_path}"
        )

    def mp4_to_mp3_conversion(self):
        """
        This function will convert avi to mp3 format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mp4_to_aac_conversion(self):
        """
        This function will convert avi to aac format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mp4_to_wav_conversion(self):
        """
        This function will convert mp4 to wav format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -f mp3 -y -minrate 256k -maxrate 256k -bufsize 256k -b:a 256k -fs 8320000  {self.output_file_path}"
        )

    def mp4_to_ogg_conversion(self):
        """
        This function will convert mp4 to ogg format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mp4_to_avi_conversion(self):
        """
        This function will convert mp4 to avi format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -vf scale=360:-1 -c:v libx264 -preset veryslow -crf 24 {self.output_file_path}"
        )

    def mp4_to_mkv_conversion(self):
        """
        This function will convert mp4 to mkv format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -vf scale=360:-1 -c:v libx264 -preset veryslow -crf 24 {self.output_file_path}"
        )

    def mp4_to_mov_conversion(self):
        """
        This function will convert mp4 to mov format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -vf scale=360:-1 -c:v libx264 -preset veryslow -crf 24 {self.output_file_path}"
        )

    def mp4_to_m4a_conversion(self):
        """
        This function will convert mp4 to m4a format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -vf scale=360:-1 -c:v libx264 -preset veryslow -crf 24 {self.output_file_path}"
        )

    def convert(self):
        try:
            if self.conversion_type == MP4_Conversion_Types.gif:
                self.mp4_to_gif_conversion()
            elif self.conversion_type == MP4_Conversion_Types.mp3:
                self.mp4_to_mp3_conversion()
            elif self.conversion_type == MP4_Conversion_Types.wav:
                self.mp4_to_wav_conversion()
            elif self.conversion_type == MP4_Conversion_Types.ogg:
                self.mp4_to_ogg_conversion()
            elif self.conversion_type == MP4_Conversion_Types.aac:
                self.mp4_to_aac_conversion()
            elif self.conversion_type == MP4_Conversion_Types.avi:
                self.mp4_to_avi_conversion()
            elif self.conversion_type == MP4_Conversion_Types.mov:
                self.mp4_to_mov_conversion()
            elif self.conversion_type == MP4_Conversion_Types.mkv:
                self.mp4_to_mkv_conversion()
            elif self.conversion_type == MP4_Conversion_Types.m4a:
                self.mp4_to_m4a_conversion()

        except Exception as e:
            raise Exception(
                f"Failed to convert MP4 to {self.conversion_type}, Reason: {str(e)}"
            )
