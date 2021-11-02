## Project Description
This dataset is based on "Bank Marketing" UCI dataset (http://archive.ics.uci.edu/ml/datasets/Bank+Marketing).

The problem I am studying is to use the bank clients' information to predict has if a client will subscribe a term deposit, and hence the bank can have some marketing strategy based on this prediction. 

## Exploratory Data Analysis (EDA):
Fortunately, the data has no missing value. For the unknown info, it is marked as NA, and I treated them as one category. 

- Used info and decribe function to have a basic analysis.
- Used Seaborn to plot the distribution of each feature
- Used DictVectorizer to convert categorical data into numerical data
- Used cross-validation to separate the data into train group and test group.

## Model Training
I used logistic regression and decision tree.

For decision tree, I tuned the parameters for max_depth and min_samples_leaf.

## Web service
-  install flask and use the host and port information in predict.py file

## Model deployment
- run predict.py (example on mac terminal: python predict.py)
- use as in Predict-test.py by _requests.post(url,json=customer).json()_
repsonse=200 means we can get the response from the service.
- instead of plain flask, we can also use gunicorn run gunicorn: gunicorn --bind 0.0.0.0:9696 predict:app

## Virtual environment with pip env
- install pipenv (pip install pipenv)
- now pipenv install all the packages needed for the production
- all the info will be stored in Pipfile
- -pipenv shell: show the directory that stored the packages 

## Docker
- find a python image: python:3.8.12-slim
- docker run -it --rm --entrypoint=bash python:3.8.12-slim then it is separated from all the other environments
- create Dockerfile: find the image, create directory, install pipenv, and copy pipenv file, copy predict and train file, expose the port, specify the entrypoint
- docker build -t [name contained Dckerfile] and then it will run Dockerfile
