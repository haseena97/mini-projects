import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("C:\\Users\Acer\Downloads\Decision Tree + Random Forest Assignment\Fraud_check.csv")
col_names = ['Undergrad', 'Marital_Status', 'Taxable_Income', 'City_Population',
       'Work_Experience', 'Urban']

data.columns = col_names
data.describe().Taxable_Income # works only for numeric data
data.info()

data.isnull().sum() # identify missing value
null_data = data[data.isnull().any(axis=1)] # kluar dkat variable
data.loc[data.isnull().any(axis=1)] # kluar kat console
data.dropna() # remove missing value
# write an Assert statement to verify really no missing, unexpected 0 or negative values
#assert that there are no missing values in the dataframe
# return Nothing if the value is True, ada value kalau mmg error
assert pd.notnull(data).all().all()

data.columns
data = data.drop(["Taxable_Income"], axis = 1)
import matplotlib.pyplot as plt
plt.hist(data.Taxable_Income)
# binning ikut quartile
# 4 interval dapat 4 category
data['sales_bin']=pd.cut(x=data['Sales'], bins=[-1,5,10,15,20], 
                        labels=["very low", " low", "medium","high"])

data['Taxable_Income_bin']=pd.cut(x=data['Taxable_Income'], bins=[1000,30000,100000], 
                        labels=["risky", " good"])
data['sales_bin'].head()
#converting into binary
lb = LabelEncoder()
data["ShelveLoc"] = lb.fit_transform(data["ShelveLoc"])
data["Urban"] = lb.fit_transform(data["Urban"])
data["US"] = lb.fit_transform(data["US"])

data_cat = data[['Undergrad', 'Marital_Status', 'Urban']]
label_encoders = {}
for column in data_cat:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column]) 
#data["default"]=lb.fit_transform(data["default"])

data['sales_bin'].unique()
data['sales_bin'].value_counts()
colnames = list(data.columns) # nak tau data type utk column
type(data.columns)

predictors = colnames[0:5] # kena simpan count utk semua x columns
target = colnames[5] # y column

# Splitting data into training and testing data set
from sklearn.model_selection import train_test_split
train,test = train_test_split(data, test_size = 0.3)

from sklearn.tree import DecisionTreeClassifier as DT

help(DT)
model = DT(criterion = 'entropy')
model.fit(train[predictors], train[target])

# Prediction on Test Data
preds = model.predict(test[predictors])
pd.crosstab(test[target], preds, rownames=['Actual'], colnames=['Predictions'])

np.mean(preds == test[target]) # Test Data Accuracy 

# Prediction on Train Data
preds = model.predict(train[predictors])
pd.crosstab(train[target], preds, rownames = ['Actual'], colnames = ['Predictions'])

np.mean(preds == train[target]) # Train Data Accuracy
