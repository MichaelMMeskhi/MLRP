from __future__ import print_function
import os
from os import walk
import PyPDF2

def pdf_to_text(pdf):
    
    pdfReader = PyPDF2.PdfFileReader(pdf)
    

dirs = ['apple', 'facebook', 'google', 'microsoft']
f = []
for d in dirs:

    mypath="/Users/ahmethamzaemra/Documents/github/MLRP/linkedin_data/"+d+"/"
    print(mypath)
    
    for dirpath, dirnames, filenames in os.walk(mypath):
        for files in filenames:
            f.append([files,d])
        
print(f)
ar = []
with open("newdata.csv", "w") as fa:
    print("path,succes, company", file=fa)
    for i in range(len(f)):
        path="".join(["resumes/",f[i][0]])
        try:
            ts=[path, "1", f[i][1]]
            print(",".join(ts) ,file=fa)
            ar.append(ts)
        except ValueError:
        	print("ops!")
        

import numpy as np 


ar = np.array(ar)

np.save('ar.npy', ar)


