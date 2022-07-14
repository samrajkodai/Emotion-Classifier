from distutils.command.config import config
import os
import argparse
from turtle import pd
from django import conf
from pkg_resources import split_sections
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import KFold
from get_data import get_data,read_params
import mlflow
from urllib.parse import urlparse
import numpy as np
from src.get_data import read_params as pd

def evaluation(x, y):
    accuracy = accuracy_score(x, y)
    matrix = confusion_matrix(x, y)

    print("accuracy : ", accuracy, '\n'"matrix : ", matrix)
    return accuracy, matrix

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

    mlflow_config = config['mlflow_config']
    remote_server_uri = mlflow_config["remote_server_uri"]

    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(mlflow_config['experiment_name'])

    with mlflow.start_run(run_name=mlflow_config['run_name']) as mlops_run:
        model=LogisticRegression()
        model.fit(x_train,y_train)

        y_pred=model.predict(x_test)
        (accuracy, matrix) = evaluation(y_test, y_pred.round())

        mlflow.log_metric("accuracy",accuracy)

        tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme

        if tracking_url_type_store != "file":
            mlflow.sklearn.log_model(
                model, 
                "model",
                 registered_model_name=mlflow_config['registered_model_name'])

        else:
            mlflow.sklearn.load_model((model,"model"))

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="config/params.yaml")
    parsed_args=args.parse_args()
    data=validation(config_path=parsed_args.config)