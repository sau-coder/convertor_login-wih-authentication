import os

from src.audio_converter.utils.Audio_Conversion_Types import M4A_Conversion_Types


class M4A_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def m4a_to_audio_conversion(self):
        """
        This function will convert m4a to aac,mp3,ogg format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def m4a_to_wav_conversion(self):
        """
        This function will convert m4a to wav format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -f mp3 -y -minrate 128k -maxrate 128k -bufsize 128k -b:a 128k -fs 89000000 {self.output_file_path}"
        )

    def convert(self):
        try:
            if self.conversion_type == M4A_Conversion_Types.wav:
                self.m4a_to_wav_conversion()
            else:
                self.m4a_to_audio_conversion()

        except Exception as e:
            raise Exception(
                f"Failed to convert M4A to {self.conversion_type}, Reason: {str(e)}"
            )
