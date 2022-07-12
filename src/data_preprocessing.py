from distutils.command.config import config
import os
import argparse
from get_data import read_params,get_data
import re
from numpy import savetxt, vectorize
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk .corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import re
from sklearn.metrics import accuracy_score,confusion_matrix,plot_confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer

def data_preprocess(config_path):
    config=read_params(config_path)
    data_path=config['data_source']['batch_files']
    df=pd.read_csv(data_path,encoding='utf-8')

    main_col=config['base']['main_col']
    target_col=config['base']['target_col']


    ##checking the missing  values
    for i in df.columns:
        if df[i].isnull().sum():
            print(i)

    corpus=[]
    ps=WordNetLemmatizer()
    for i in range(0, len(df[main_col])):
        print(i)
        review = re.sub('[^a-zA-Z]', ' ', df[main_col][i])
        review = review.lower()
        review = review.split()
        
        review = [ps.lemmatize(word) for word in review if not word in stopwords.words('english')]
        review = ' '.join(review)
        corpus.append(review)

    
    

    y=df[target_col]
    
    vectorizer=CountVectorizer()
    x=vectorizer.fit_transform(corpus).toarray()
    

    x_csv=config['load_data']['x_csv']
    y_csv=config['load_data']['y_csv']

    raw_data_path=config["load_data"]["raw_dataset_csv"]
    x=np.save(x_csv, x)
    y=np.save(y_csv, y)



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="config/params.yaml")
    parsed_args=args.parse_args()
    data=data_preprocess(config_path=parsed_args.config)