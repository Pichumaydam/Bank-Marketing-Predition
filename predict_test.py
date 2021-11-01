import requests

url='http://localhost:9696/predict'

customer={'age': 27,
 'job': 'student',
 'marital': 'single',
 'education': 'university.degree',
 'default': 'yes',
 'housing': 'no',
 'loan': 'no',
 'contact': 'cellular',
 'month': 'may',
 'day_of_week': 'mon',
 'duration': 55,
 'campaign': 3,
 'pdays': 999,
 'previous': 0,
 'poutcome': 'nonexistent',
 'emp.var.rate': 1.1,
 'cons.price.idx': 93.994,
 'cons.conf.idx': -36.4,
 'euribor3m': 4.857,
 'nr.employed': 5191.0,
 'y': 0}


response=requests.post(url,json=customer).json()

if response['churn']==True:
    print('sending promo to %s' %('xyz-123'))
else:
    print('do not sending promo to %s' %('xyz-123'))


