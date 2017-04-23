import pandas as pd 
import numpy as np 
import re 
import os
import PyPDF2
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from flask import render_template, Flask, request
import flask 
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer




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


## Geting ready the training data 
data=pd.read_csv('resumes.csv')
X_train=[]
for i in data['path']:

    pdf = open(i, 'rb')
    X_train.append(pdf_to_text(pdf))

count_vect = CountVectorizer(lowercase = False, max_df = .6)
tfidf_transformer = TfidfTransformer()
X_train_counts = count_vect.fit_transform(X_train)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

## classifier
clf = BernoulliNB(alpha = .3)
clf.fit(X_train_tfidf,data['succes'])

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
        result= getPredictions(clf,count_vect,tfidf_transformer,X_test)

    if result[0]==1:
        return render_template("result.html" ,sonuc="1")
    elif result[0]==2:
        return render_template("result.html", sonuc="2")# waiting for tiers 

    
    
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5003  )