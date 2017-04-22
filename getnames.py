from __future__ import print_function
import os
from os import walk

mypath="C:\\Users\\aemra\\Documents\\GitHub\\MLRP\\resumes\\2"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
print(f)

with open("resumes2.csv", "w") as fa:
    print("path,succes", file=fa)
    for i in range(len(f)):
        path="".join(["resumes\\",f[i]])
        ts=[path, "2"]
        
        print(",".join(ts) ,file=fa)