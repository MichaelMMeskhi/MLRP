import pandas as pd
import numpy as np
import re
import os
import PyPDF2
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.cluster import KMeans
from flask import render_template, Flask, request
import flask

stemmer=SnowballStemmer("english")
def pdf_to_text(pdf):

    pdfReader = PyPDF2.PdfFileReader(pdf)
    numPage=pdfReader.numPages
    pdftext=" "
    for page in range(numPage):
        pageObj =pdfReader.getPage(page)
        text= pageObj.extractText()
        pagetext="".join(text)
        pdftext=" ".join([pagetext, pdftext])
    alltext = re.sub('[\n]', '', pdftext)
    all_words=alltext.split(" ")
    affterstemmer=[]
    for word in all_words:
        affterstemmer.append(stemmer.stem(word))
    stop = set(stopwords.words('english'))
    afterstop=[]
    for word in affterstemmer:
        if word not in stop:
            afterstop.append(word)
    return " ".join(afterstop)
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


## Geting ready the training data
data=pd.read_csv('resumes.csv')
X_train=[]
for i in data['path']:
    my_file = os.path.join(THIS_FOLDER, i)
    pdf = open(my_file, 'rb')
    X_train.append(pdf_to_text(pdf))



count_vect = CountVectorizer(lowercase = False, min_df = 0.001)
tfidf_transformer = TfidfTransformer(smooth_idf=False)
X_train_counts = count_vect.fit_transform(X_train)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)



# K-means model
kmeans = KMeans(n_clusters=2,  max_iter=100 , random_state=0).fit(X_train_tfidf)
cl = kmeans.labels_
count=0
for i in range(len(cl)):
    if cl[i]!=data['succes'][i]-1:
        #print(data['path'][i])
        count+=1
print(cl)
print(count/len(cl))


def getPredictions(clf,count_vect,tfidf_transformer,X_test):

    #do the training

    X_test_counts = count_vect.transform(X_test)
    X_test_tfidf = tfidf_transformer.transform(X_test_counts)

    return clf.predict(X_test_tfidf)


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath("app.py"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, "testresumes/")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)


    for file in request.files.getlist("file"):
        text=pdf_to_text(file)
        X_test=[]
        X_test.append(text)
        result= getPredictions(kmeans,count_vect,tfidf_transformer,X_test)

    if result[0]==0:
        return render_template("result.html" ,sonuc="Your resume looks great! Here are some companies, You may want to consider: Apple, Hewlett-Packard, IBM, Amazon, Microsoft, Google, Intel, Cisco Systems, Oracle, Qualcomm, EMC, Xerox, Danaher, eBay, Uber, Plantair, Snapchat, Github, HackerRank, Twitter, Facebook, Texas Instruments, Quora, Intuit, Infosys, LinkedIn, Yahoo!, Kaspersky, Nvidia, AMD")
    elif result[0]==1:
        return render_template("result.html", sonuc="Your resume looks good but you need some improvement. Get experience from this companies: BMC Software, Pros Holding Inc., NetIQ, Quorum Business Solutions Inc, Alert Logic Inc., HCSS.")# waiting for tiers




    return render_template("index.html")

if __name__ == "__main__":
    app.run()
