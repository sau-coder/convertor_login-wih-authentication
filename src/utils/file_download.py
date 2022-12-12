import datetime
import os
import shutil
import uuid

from src.config.config import STATIC_FILE


# Save File locally
def save_file(file):
    try:

        date = datetime.datetime.now()
        time_stamp = int(datetime.datetime.timestamp(date) * 1000)
        id = str(uuid.uuid4())
        folder_name = f"{STATIC_FILE}{time_stamp}-{id}"
        os.makedirs(folder_name)

        # set filename
        extension = file.filename.split(".")[-1]
        file_name = str(id + "." + extension)

        # Open File and save as binary
        with open(f"{folder_name}/{file_name}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    except Exception:
        raise Exception("File Error Occured")

    return file_name, folder_name
