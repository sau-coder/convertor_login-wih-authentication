from enum import Enum


class Conversion_Types(str, Enum):
    mp3 = "mp3"
    m4a = "m4a"
    aac = "aac"
    wav = "wav"
    ogg = "ogg"


class MP3_Conversion_Types(str, Enum):
    aac = "aac"
    m4a = "m4a"
    ogg = "ogg"
    wav = "wav"


class M4A_Conversion_Types(str, Enum):
    mp3 = "mp3"
    aac = "aac"
    ogg = "ogg"
    wav = "wav"


class AAC_Conversion_Types(str, Enum):
    mp3 = "mp3"
    m4a = "m4a"
    ogg = "ogg"
    wav = "wav"


class WAV_Conversion_Types(str, Enum):
    aac = "aac"
    m4a = "m4a"
    ogg = "ogg"
    mp3 = "mp3"


class OGG_Conversion_Types(str, Enum):
    aac = "aac"
    m4a = "m4a"
    mp3 = "mp3"
    wav = "wav"
