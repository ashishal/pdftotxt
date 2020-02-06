# ////////  INSTALLATION OF TEXTRACT \\\\\\\\
#             Extracts texts from files

# apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
# flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev
# pip3 install textract


# ////////  INSTALLATION OF TABULA \\\\\\\\
# pip3 installl tabula


import textract
import pandas as pd
import tabula
import os
from os import listdir

def textfrompdf():
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
        # print(text)

def tablefrompdf():
    file_path="pdfs"
    outputfolder="tables"
    pdf_files=listdir(file_path)

    for pdfs in pdf_files:
        pdf_path=os.path.join(file_path,pdfs)
        datatable=tabula.read_pdf(pdf_path, multiple_tables=True, encoding='utf-8', pages='all')
        df=pd.DataFrame(datatable)
        output_file_name = os.path.splitext(pdfs)[0]
        output_file=os.path.join(outputfolder,output_file_name)
        df.to_csv(output_file+'.csv', mode='w',index=False)
        
        # tabula.convert_into(pdf_path, output_file+'.csv', output_format="csv",multiple_tables=True, pages='all')
        

if __name__== "__main__":
    textfrompdf()
    tablefrompdf()
    
