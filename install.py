import os

import nltk
import spacy

# install necessary packages
os.system("sudo apt-get install -y")
os.system("sudo apt-get update -y")
os.system("sudo apt install default-jre -y")
os.system("sudo apt install libreoffice -y")
os.system("sudo apt install ffmpeg -y")
os.system("sudo apt install inkscape -y")
os.system("sudo apt install pdf2svg -y")


# install spacy model
spacy.cli.download("en_core_web_sm")

# to install punkt
nltk.download("punkt")
