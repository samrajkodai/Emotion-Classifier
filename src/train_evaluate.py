from distutils.command.config import config
import os
import argparse
from turtle import pd
from django import conf
from pkg_resources import split_sections
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from get_data import get_data,read_params

import numpy as np
from src.get_data import read_params as pd


def validation(config_path):
    config=read_params(config_path)

    x_test_data_path = config["split_data"]["x_test_path"]
    x_train_data_path = config["split_data"]["x_train_path"]
    y_test_data_path = config["split_data"]["y_test_path"]
    y_train_data_path = config["split_data"]["y_train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]
    x_train = np.load(x_train_data_path, allow_pickle=True)
    x_test = np.load(x_test_data_path, allow_pickle=True)
    y_train = np.load(y_train_data_path, allow_pickle=True)
    y_test = np.load(y_test_data_path, allow_pickle=True)

    split_size=config['split_data']['test_size']


    model=LogisticRegression()
    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    print(y_pred)

    print(accuracy_score(y_test,y_pred))

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="config/params.yaml")
    parsed_args=args.parse_args()
    data=validation(config_path=parsed_args.config)