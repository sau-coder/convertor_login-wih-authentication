# Extension checker


def extension_checker(file_name):
    extension = file_name.split(".")[1]

    if extension == "docx" or extension == "doc":
        response = "docx"

    elif extension == "xlsx" or extension == "xls":
        response = "xlsx"

    elif extension == "jpg" or extension == "jpeg":
        response = "jpg"

    elif extension == "pdf":
        response = "pdf"

    elif extension == "png":
        response = "png"

    elif extension == "webp":
        response = "webp"

    elif extension == "json":
        response = "json"

    elif extension == "csv":
        response = "csv"

    elif extension == "yaml" or extension == "yml":
        response = "yaml"

    elif extension == "xml":
        response = "xml"

    elif extension == "tsv":
        response = "tsv"

    elif extension == "jpg" or extension == "jpeg":
        response = "jpg"

    elif extension == "mp4":
        response = "mp4"

    elif extension == "avi":
        response = "avi"

    elif extension == "svg":
        response = "svg"

    elif extension == "tiff":
        response = "tiff"

    elif extension == "vsd":
        response = "vsd"

    elif extension == "psd":
        response = "psd"

    elif extension == "mov":
        response = "mov"

    elif extension == "mkv":
        response = "mkv"

    elif extension == "mp3":
        response = "mp3"

    elif extension == "m4a":
        response = "m4a"

    elif extension == "aac":
        response = "aac"

    elif extension == "wav":
        response = "wav"

    elif extension == "ogg":
        response = "ogg"

    elif extension == "vsdx":
        response = "vsdx"

    elif extension == "bmp":
        response = "bmp"

    elif extension == "emf":
        response = "emf"

    elif extension == "heic":
        response = "heic"

    else:
        response = extension
    return response
