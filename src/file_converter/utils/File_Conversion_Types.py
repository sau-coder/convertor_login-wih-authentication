from enum import Enum


class Conversion_Types(str, Enum):
    csv = "csv"
    tsv = "tsv"
    xlsx = "xlsx"
    json = "json"
    xml = "xml"
    yaml = "yaml"


class CSV_Conversion_Types(str, Enum):
    xlsx = "xlsx"
    html = "html"
    json = "json"
    tsv = "tsv"
    xml = "xml"


class TSV_Conversion_Types(str, Enum):
    csv = "csv"


class EXCEL_Conversion_Types(str, Enum):
    csv = "csv"
    json = "json"


class JSON_Conversion_Types(str, Enum):
    csv = "csv"
    xlsx = "xlsx"
    xml = "xml"
    yaml = "yaml"


class XML_Conversion_Types(str, Enum):
    csv = "csv"
    xlsx = "xlsx"
    json = "json"


class YAML_Conversion_Types(str, Enum):
    json = "json"
