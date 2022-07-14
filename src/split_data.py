import os
from get_data import get_data, read_params
import argparse
from sklearn.model_selection import train_test_split
import os
import pandas as pd
from numpy import load
import numpy as np


def split_train_test(config_path):
    config = read_params(config_path)
    x_train_data_path = config["split_data"]["x_train_path"]
    x_test_data_path = config["split_data"]["x_test_path"]
    y_train_data_path = config["split_data"]["y_train_path"]
    y_test_data_path = config["split_data"]["y_test_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    x_csv_path = config['load_data']['x_csv']
    y_csv_path = config['load_data']['y_csv']
    x = load(x_csv_path, allow_pickle=True)
    y = load(y_csv_path, allow_pickle=True)

    df = pd.read_csv(raw_data_path, sep=",")
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=split_ratio, random_state=random_state)

    x_train = np.save(x_train_data_path, x_train)
    x_test = np.save(x_test_data_path, x_test)
    y_train = np.save(y_train_data_path, y_train)
    y_test = np.save(y_test_data_path, y_test)



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="config/params.yaml")
    parsed_args=args.parse_args()
    data=split_train_test(config_path=parsed_args.config)