import pandas as pd
import glob
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def modify(text):
    if type(text) is not str :
        return []
    
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    lowercased =  text.lower()
    
    special_full_stop = re.sub(r'\.(?=\w)','. ', lowercased)
    no_punct = re.sub(r'[^A-Za-z\s]', '', special_full_stop)
    tokens = nltk.word_tokenize(no_punct)
    
    stop_words = set(stopwords.words('english'))
    no_stopwords = [w for w in tokens if not w in stop_words]
       
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w) for w in no_stopwords]
    return lemmatized



filename = 'titles.csv'
titleset = pd.read_csv(filename)

'''print(titleset['description'].head())'''

description = titleset['description']
description = description.apply(modify)

print(description)

    
    






