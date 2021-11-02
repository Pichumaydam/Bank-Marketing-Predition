# Midterm-Project

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

## Model deployment

