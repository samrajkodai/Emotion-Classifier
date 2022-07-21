
#   Emotion Classifier.

![6428f74d-40b2-4026-be26-dd088b542a52](https://user-images.githubusercontent.com/61903698/180166677-bfb13515-6007-4051-8b57-73aa3cc1e4f4.gif)


for live project you can visit https://emotionclass.herokuapp.com/

## <a href="url"><img src="https://user-images.githubusercontent.com/61903698/178228250-a11a8416-3443-4c90-8616-8eda1edc4572.jpg" align="left" height="48" width="48" ></a>Description
* Emotion Classifier created as an AI module Integrated with webapp
by using NLP, Machine Learning and Flask API.
* Created as a proof of concept (POC) and the aim is to find users
emotions.

## <a href="url"><img src="https://user-images.githubusercontent.com/61903698/178230062-a2e8bf94-4769-4e02-a26b-ed3696aae3fe.png" align="left" height="48" width="48" ></a>Dataset
you can download and use the dataset from kaggle please visit this link to download the dataset

https://www.kaggle.com/search?q=spam+email+in%3Adatasets](https://www.kaggle.com/datasets/ozlerhakan/spam-or-not-spam-dataset)

## <a href="url"><img src="https://user-images.githubusercontent.com/61903698/178229350-7f29d4eb-e758-455d-ab8e-87ef337e1880.png" align="left" height="48" width="48" ></a> Installation

### Libraries
* dvc
* dvc[gdrive]
* sklearn
* pandas
* pytest
* tox
* flake8
* flask
* gunicorn
* PyYAML
* nltk
* mlflow
* pickle5==0.0.1

to install above libraries please run the command

```bash
     pip install requirements.txt
```




##  <a href="url"><img src="https://user-images.githubusercontent.com/61903698/178230859-ca0b335b-1792-456a-a535-2a0462361e75.png" align="left" height="48" width="48" ></a>  Deployment

To deploy this project run

```bash
  python src/get_data.py
  python src/load_data.py
  python src/data_preprocessing.py
  python src/split_data.py
  python src/train_evaluate.py 
```

#### Git Commands
```bash
     git remote add origin https://github.com/<your git>/<app name>.git
     git add .
     git commit -m "your text"
     git branch -M main   
     git push -m origin main

```


## <a href="url"><img src="https://user-images.githubusercontent.com/61903698/178232811-59ccbc05-50da-4f46-8b4a-e2f9c9d79201.png" align="left" height="48" width="48" ></a> Screenshots


<img src="https://user-images.githubusercontent.com/61903698/179744083-e4a3f62f-2395-47ad-b3b7-6e0ff9256574.jpeg" width=40% height=0%>



## <a href="url"><img src="https://user-images.githubusercontent.com/61903698/178231990-81b6bcce-dbaa-4180-b363-dcc694e76a1e.png" align="left" height="48" width="48" ></a>  Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


## AI Tools and Framework
* Machine Learning
* Deep Learning
* LSTM
* Natural Language Processing
* Flask
* Mlops
* Dvc
* Git
* Vscode


## <a href="url"><img src="https://user-images.githubusercontent.com/61903698/178233478-e078e157-5156-4a29-a784-565395329de1.jpg" align="left" height="48" width="48" ></a> Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

