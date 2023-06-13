# Importing the libraries
import numpy as np
import pandas as pd
import pickle

dataset = pd.read_csv('../test_app_data/synthetic_data.csv')

x = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y = train_test_split(x,y, random_state = 101)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

# Fitting model with trainig data
regressor.fit(train_x, train_y)

# Saving model to disk
print("Saving model to disk")
pickle.dump(regressor, open('model.pkl','wb'))

'''
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6]]))
'''