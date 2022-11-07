import pandas as pd
# import numpy as np

#Importing Data, sep=ikut delimiter jenis apa
claimants1 = pd.read_csv("C:\\Users\\Acer\\Downloads\\Affairs (1)\\Bank.csv", sep=";")

#removing CASENUM column
claimants1 = claimants1.drop('CASENUM', axis=1)
claimants1.head(11) # 11 value pertama
claimants1.columns
#df_num = training[['Age','SibSp','Parch','Fare']]
claimants1_num = claimants1[['duration', 'age', 'campaign','default','pdays','loan','contact','poutcome','y']]
claimants1_cat = claimants1[['job', 'marital', 'education','default','housing','loan','contact','poutcome','y']]
from sklearn.preprocessing import LabelEncoder
label_encoders = {}
categorical_columns = [0, 1, 2, 3]  # I would recommend using columns names here if you're using pandas. If you're using numpy then stick with range(n) instead

for column in claimants1_cat:
    label_encoders[column] = LabelEncoder()
    claimants1[column] = label_encoders[column].fit_transform(claimants1[column]) 
claimants1['poutcome'].value_counts()
claimants1['day'].value_counts()
# barplot
import seaborn as sns
import matplotlib.pyplot as plt
for i in claimants1_cat.columns:
   # plt.figure(figsize=(11,6))
    sns.barplot(claimants1_cat[i].value_counts().index,claimants1_cat[i].value_counts()).set_title(i)
    plt.show()
   
for i in claimants1.columns:
       # plt.figure(figsize=(11,6))
        sns.barplot(claimants1[i].value_counts().index,claimants1[i].value_counts()).set_title(i)
        plt.show()
# binary encoding
claimants1['default'] = claimants1['default'].apply(lambda x: 1 if x == 'yes' else 0)
claimants1['housing'] = claimants1['housing'].apply(lambda x: 1 if x == 'yes' else 0)
claimants1['loan'] = claimants1['loan'].apply(lambda x: 1 if x == 'yes' else 0)
claimants1['y'] = claimants1['y'].apply(lambda x: 1 if x == 'yes' else 0)
# pivot table
pivot1 = pd.pivot_table(claimants1,index='y',columns='day', values = 'marital', aggfunc='count')

# since nak tau akan ada affair ke x, so kena buat binary encoding jugak
# label encode utk nominal
origin_series = pd.Series(claimants1.marital)
cat_house = origin_series.astype('category')
from sklearn.preprocessing import LabelEncoder
lb_make = LabelEncoder()
marital_encoded = lb_make.fit_transform(cat_house)
claimants1['maritalcoded'] = marital_encoded
# nak masukkan terus dalam column training data
house['statecoded'] = house_encoded

origin_series = pd.Series(claimants1.contact)
cat_house = origin_series.astype('category')
from sklearn.preprocessing import LabelEncoder
lb_make = LabelEncoder()
educ_encoded = lb_make.fit_transform(cat_house)
claimants1['con_encoded']= educ_encoded
# nak masukkan terus dalam column training data
house['con_ecoded'] = house_encoded
import numpy as np
claimants1["affairs2"] = np.where(claimants1["affairs"] >1, 1,claimants1['affairs'])

### Splitting the data into train and test data 
from sklearn.model_selection import train_test_split
train_data,test_data = train_test_split(claimants1, test_size = 0.30) # 30% test data

# Model building 
import statsmodels.formula.api as sm # ytrain ~ xtrain
logit_model = sm.logit('y ~ age+job+marital+education+default+balance+housing+loan+contact+day+month+duration+campaign+pdays+previous+poutcome', data = train_data).fit()
# log_regression.fit(X_train,y_train)
#summary
logit_model.summary()

## Evaluation of the model
predict_test = logit_model.predict(pd.DataFrame(test_data[['age', 'job', 'marital', 'education', 'default', 'balance', 'housing','loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays','previous', 'poutcome']]))

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
# tgk confusion matrix
cnf_test_matrix = confusion_matrix(test_data['y'], predict_test > 0.5 )
cnf_test_matrix

print(accuracy_score(test_data.y, predict_test > 0.5))

## Error on train data
predict_train = logit_model.predict(pd.DataFrame(train_data[['age', 'job', 'marital', 'education', 'default', 'balance', 'housing','loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays','previous', 'poutcome']]))

cnf_train_matrix = confusion_matrix(train_data['y'], predict_train > 0.5 )
cnf_train_matrix

print(accuracy_score(train_data.y, predict_train > 0.5))

#define metrics
from sklearn import metrics
#y_pred_proba = log_regression.predict_proba(test_data[['gender','age','yearsmarried','children','religiousness','education','occupation','rating']])[::,1]
fpr, tpr, _ = metrics.roc_curve(test_data['affairs2'],  predict_test)
#fpr, tpr, _ = metrics.roc_curve(test_data['affairs2'],  y_pred_proba)
import matplotlib.pyplot as plt
#create ROC curve
plt.plot(fpr,tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
auc = metrics.roc_auc_score(test_data['affairs2'],  predict_test)

#create ROC curve
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()