from flask import Flask,redirect,url_for,request,render_template
import numpy as np
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import tensorflow as tf
import os
from keras.models import load_model
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
import yaml
import pickle

params_path="config/params.yaml"



def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config


def predict(data):
  config=read_params(params_path)
  predict_path=config['pickle']['classifier_pkl']
  cv_path=config['pickle']['cv_transform_pkl']

  clas=pickle.load(open(predict_path,'rb'))
  cv=pickle.load(open(cv_path,'rb'))
  data=[data]
  x=cv.transform(data).toarray()
  s=clas.predict(x)

  
  if s==0:
    return "fear 😨😨😨😨"
  elif s==1:
    return "anger 😡😡😡😡"
  elif s==2:
    return 'joy 😂😂😂😂'
  elif s==3:
    return "sad 😔😔😔😔"
  else:
    return "sorry"



# def predict(data):

#   print(data)
#   config=read_params(params_path)

  

#   data=[data]

#   data=cv.transform(data).toarray()
  
#   print(data)
#   res=clas.predict(data)[0]

#   print(res)
#   print(type(res))

#   if res==0:
#     return "fear 😨😨😨😨"
#   elif res==1:
#     return "anger 😡😡😡😡"
#   elif res==2:
#     res='joy 😂😂😂😂' 
#   elif res==3:
#     return "sad 😔😔😔😔"
#   else:
#     return "sorry"