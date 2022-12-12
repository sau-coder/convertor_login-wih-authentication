from enum import Enum


class Conversion_Types(str, Enum):
    jpg = "jpg"
    png = "png"
    webp = "webp"
    psd = "psd"
    tiff = "tiff"
    svg = "svg"
    vsd = "vsd"
    vsdx = "vsdx"
    bmp = "bmp"
    heic = "heic"


class JPG_Conversion_Types(str, Enum):
    pdf = "pdf"
    png = "png"
    webp = "webp"
    bmp = "bmp"
    eps = "eps"
    tiff = "tiff"


class PNG_Conversion_Types(str, Enum):
    jpg = "jpg"
    pdf = "pdf"
    bmp = "bmp"
    eps = "eps"
    tiff = "tiff"
    webp = "webp"


class WEBP_Conversion_Types(str, Enum):
    jpg = "jpg"
    png = "png"
    bmp = "bmp"
    eps = "eps"
    pdf = "pdf"
    webp = "webp"


class PSD_Conversion_Types(str, Enum):
    png = "png"
    jpg = "jpg"
    bmp = "bmp"
    eps = "eps"
    pdf = "pdf"
    tiff = "tiff"
    webp = "webp"


class TIFF_Conversion_Types(str, Enum):
    png = "png"
    jpg = "jpg"
    svg = "svg"
    docx = "docx"
    text = "txt"
    bmp = "bmp"
    pdf = "pdf"


class SVG_Conversion_Types(str, Enum):
    png = "png"
    jpg = "jpg"
    tiff = "tiff"
    docx = "docx"
    text = "txt"
    bmp = "bmp"
    emf = "emf"
    pdf = "pdf"


class VSD_Conversion_Types(str, Enum):
    pdf = "pdf"
    png = "png"
    tiff = "tiff"
    jpg = "jpg"
    bmp = "bmp"
    emf = "emf"
    docx = "docx"
    pptx = "pptx"
    eps = "eps"
    webp = "webp"
    text = "txt"
    svg = "svg"
    heic = "heic"
    psd = "psd"
    vsdx = "vsdx"


class VSDX_Conversion_Types(str, Enum):
    pdf = "pdf"
    png = "png"
    tiff = "tiff"
    jpg = "jpg"
    bmp = "bmp"
    emf = "emf"
    docx = "docx"
    pptx = "pptx"
    eps = "eps"
    webp = "webp"
    text = "txt"
    svg = "svg"
    heic = "heic"
    psd = "psd"
    vsd = "vsd"


class BMP_Conversion_Types(str, Enum):
    jpg = "jpg"
    png = "png"
    tiff = "tiff"
    pdf = "pdf"
    emf = "emf"
    svg = "svg"
    docx = "docx"


class HEIC_Conversion_Types(str, Enum):
    png = "png"
    bmp = "bmp"
    eps = "eps"
    jpg = "jpg"
    pdf = "pdf"
    tiff = "tiff"
    webp = "webp"
