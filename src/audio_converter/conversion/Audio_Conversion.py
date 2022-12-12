from src.audio_converter.conversion.AAC_Conversion import AAC_Conversion
from src.audio_converter.conversion.M4A_Conversion import M4A_Conversion
from src.audio_converter.conversion.MP3_Conversion import MP3_Conversion
from src.audio_converter.conversion.OGG_Conversion import OGG_Conversion
from src.audio_converter.conversion.WAV_Conversion import WAV_Conversion
from src.audio_converter.utils.Audio_Conversion_Types import Conversion_Types


class Audio_Conversion:
    def __init__(self, input_file_path, output_file_path, conversion_type, type):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.conversion_type = conversion_type
        self.type = type

    def converter(self):
        if self.type == Conversion_Types.mp3:
            mp3_conversion_object = MP3_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            mp3_conversion_object.convert()

        elif self.type == Conversion_Types.wav:
            wav_conversion_object = WAV_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            wav_conversion_object.convert()

        elif self.type == Conversion_Types.ogg:
            ogg_conversion_object = OGG_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            ogg_conversion_object.convert()

        elif self.type == Conversion_Types.aac:
            aac_conversion_object = AAC_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            aac_conversion_object.convert()

        elif self.type == Conversion_Types.m4a:
            m4a_conversion_object = M4A_Conversion(
                input_file_path=self.input_file_path,
                output_file_path=self.output_file_path,
                conversion_type=self.conversion_type,
            )
            m4a_conversion_object.convert()
