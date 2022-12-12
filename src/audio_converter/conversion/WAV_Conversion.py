import os

from src.audio_converter.utils.Audio_Conversion_Types import WAV_Conversion_Types


class WAV_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type

    def wav_to_audio_conversion(self):
        """
        This function will convert wav to aac,m4a,mp3 format.
        """
        os.system(f"ffmpeg -i {self.input_file_path} {self.output_file_path}")

    def wav_to_ogg_conversion(self):
        """
        This function will convert wav to ogg format.
        """
        os.system(
            f"ffmpeg -i {self.input_file_path} -f mp3 -y -minrate 128k -maxrate 128k -bufsize 128k -b:a 128k -fs 89000000 {self.output_file_path}"
        )

    def convert(self):
        try:
            if self.conversion_type == WAV_Conversion_Types.ogg:
                self.wav_to_ogg_conversion()
            else:
                self.wav_to_audio_conversion()
        except Exception as e:
            raise Exception(
                f"Failed to convert WAV to {self.conversion_type}, Reason: {str(e)}"
            )
