import os
from sys import platform

if platform == "linux" or platform == "linux2":
    CWD = os.getcwd()
    STATIC_FILE = f"{CWD}/static/"
    LIBRE_OFFICE = "libreoffice"

elif platform == "win32":
    CWD = os.getcwd()
    STATIC_FILE = f"{CWD}\\static\\"
    LIBRE_OFFICE = "C:/LibreOffice/program/soffice.com"
