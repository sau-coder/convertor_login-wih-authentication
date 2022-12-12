from enum import Enum


class Conversion_Types(str, Enum):
    pdf = "pdf"
    docx = "docx"


class PDF_Conversion_Types(str, Enum):
    csv = "csv"
    docx = "docx"
    txt = "txt"
    xlsx = "xlsx"
    encrypt_pdf = "encrypt_pdf"
    decrypt_pdf = "decrypt_pdf"
    png = "png"
    jpg = "jpg"
    emf = "emf"
    svg = "svg"


class DOC_Conversion_Types(str, Enum):
    doc = "doc"
    docx = "docx"
    pdf = "pdf"
    txt = "txt"
