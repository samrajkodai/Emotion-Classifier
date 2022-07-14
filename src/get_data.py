import argparse
from distutils.command.config import config
import os
import yaml
import pandas as pd

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
        return config

def get_data(config_path):
    config=read_params(config_path)
    data_path=config['data_source']['batch_files']
    df=pd.read_csv(data_path,encoding='utf-8')

    raw_data_path=config["load_data"]["raw_dataset_csv"]

    df.to_csv(raw_data_path,sep=",",index=False)

    return df

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="config/params.yaml")
    parsed_args=args.parse_args()
    data=get_data(config_path=parsed_args.config)