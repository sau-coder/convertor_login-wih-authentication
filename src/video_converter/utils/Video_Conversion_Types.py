from enum import Enum


class Conversion_Types(str, Enum):
    mp4 = "mp4"
    mov = "mov"
    mkv = "mkv"
    avi = "avi"


class MP4_Conversion_Types(str, Enum):
    gif = "gif"
    mp3 = "mp3"
    wav = "wav"
    ogg = "ogg"
    aac = "aac"
    avi = "avi"
    mov = "mov"
    mkv = "mkv"
    m4a = "m4a"


class MOV_Conversion_Types(str, Enum):
    gif = "gif"
    mp3 = "mp3"
    aac = "aac"
    wav = "wav"
    ogg = "ogg"
    avi = "avi"
    mkv = "mkv"
    m4a = "m4a"
    mp4 = "mp4"


class MKV_Conversion_Types(str, Enum):
    gif = "gif"
    mp3 = "mp3"
    mp4 = "mp4"
    wav = "wav"
    ogg = "ogg"
    avi = "avi"
    mov = "mov"
    aac = "aac"


class AVI_Conversion_Types(str, Enum):
    gif = "gif"
    mp3 = "mp3"
    mp4 = "mp4"
    wav = "wav"
    ogg = "ogg"
    mkv = "mkv"
    mov = "mov"
    aac = "aac"
