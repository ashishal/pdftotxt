# ////////  INSTALATION OF TEXTRACT \\\\\\\ \

# apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
# flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev
# pip3 install textract

import textract
import os
from os import listdir

file_path="pdfs"
outputpath="txts"
pdf_files=listdir(file_path)

for pdfs in pdf_files:
    pdf_path=os.path.join(file_path,pdfs)
    text=textract.process(pdf_path,method='tesseract')
    output_file_name = os.path.splitext(pdfs)[0]
    f=open(os.path.join(outputpath,output_file_name+'.txt'),"wt")
    texts=str(text)
    f.write(texts)
    print(text)
