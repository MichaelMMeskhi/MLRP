from __future__ import print_function
import os
from os import walk
import PyPDF2


def pdf_to_text(pdf):
    
    pdfReader = PyPDF2.PdfFileReader(pdf)
    



mypath="C:\\Users\\aemra\\Documents\\GitHub\\MLRP\\resumes\\1"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
print(f)

with open("resumes1.csv", "w") as fa:
    print("path,succes", file=fa)
    for i in range(len(f)):
        path="".join(["resumes\\1\\",f[i]])
        try:
        	pdf=open(path, "rb")
        	pdfReader = PyPDF2.PdfFileReader(pdf)

        	ts=[path, "1"]
        
        	print(",".join(ts) ,file=fa)
        except ValueError:
        	print("ops!")
        




