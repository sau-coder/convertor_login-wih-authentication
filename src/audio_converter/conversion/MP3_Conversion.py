import os

from src.audio_converter.utils.Audio_Conversion_Types import MP3_Conversion_Types


class MP3_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def mp3_to_audio_conversion(self):
        """
        This function will convert mp3 to aac, ogg, m4a format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def mp3_to_wav_conversion(self):
        """
        This function will convert mp3 to wav format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -f mp3 -y -minrate 128k -maxrate 128k -bufsize 128k -b:a 128k -fs 89000000 {self.output_file_path}"
        )

    def convert(self):
        try:
            if self.conversion_type == MP3_Conversion_Types.wav:
                self.mp3_to_wav_conversion()
            else:
                self.mp3_to_audio_conversion()

        except Exception as e:
            raise Exception(
                f"Failed to convert MP3 to {self.conversion_type}, Reason: {str(e)}"
            )
