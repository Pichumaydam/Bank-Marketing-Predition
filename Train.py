import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

import pickle


# parameters
C = 1.0
n_splits = 5

output_file=f'model_C={C}.bin'

# data preparation

df = pd.read_csv('bank-additional-full.csv',sep=';')

df.y = (df.y == 'yes').astype(int)
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
numerical=['age','duration','campaign','pdays','previous','emp.var.rate','cons.price.idx','cons.conf.idx','euribor3m','nr.employed']
categorical=['job',
 'marital',
 'education',
 'default',
 'housing',
 'loan',
 'contact',
 'month',
 'day_of_week',
 'poutcome']
# training

def train(df_train, y_train, C=1.0):
    dicts = df_train[categorical + numerical].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    
    return dv, model

def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

print(f'doing validation with C={C}')


# validation

kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)

scores = []

fold=0
for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.y.values
    y_val = df_val.y.values

    dv, model = train(df_train, y_train, C=C)
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)

    print(f'auc on fold {fold} is {auc}')
    fold=fold+1

print('validation results:')
print('C=%s %.3f +- %.3f'%(C,np.mean(scores),np.std(scores)))

# training the final model

print('training the final model')
dv, model = train(df_full_train, df_full_train.y.values, C=1.0)
y_pred = predict(df_test, dv, model)

y_test = df_test.y.values
auc = roc_auc_score(y_test, y_pred)
print(f'auc={auc}')


# save the model

with open(output_file,'wb') as f_out:
    pickle.dump((dv,model),f_out)

print(f'the model is saved to {output_file}')


