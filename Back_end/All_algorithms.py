import pandas as pd
from sklearn import preprocessing
import json
from ast import literal_eval
import ast
import numpy as np

#---For printing data
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


mapper={}
def PrepareData(df):
    df.fillna(0, inplace=True)
    categorical_list = list(df.columns.values)
    categorical_list.remove('class')
    newdf = pd.DataFrame(columns=categorical_list)
    for x in categorical_list:
        mapper[x]=preprocessing.LabelEncoder()
    for x in categorical_list:
        if (df.dtypes[x]==object):
            newdf[x]= mapper[x].fit_transform(df.__getattr__(x).astype(str))
        else:
            newdf[x]=df.__getattr__(x)
    le = preprocessing.LabelEncoder()
    #myclass = le.fit_transform(df.__getattr__('class'))
    myclass=df.__getattr__('class')
    #newdf is the dataframe with all columns except class column and myclass is the class column
    return newdf, myclass , categorical_list


from sklearn.metrics import accuracy_score
dataset1 = pd.read_csv('dataset.csv',delimiter=',')

dataset={"data":"",
         "target":""}

dataset["data"],dataset["target"],columns = PrepareData(dataset1)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dataset["data"], dataset["target"], test_size=0.2, shuffle=False)


def erreur2(test_data,test_target):
    return (1-accuracy_score(test_data,test_target))

def test(nb):
    nb.fit(X_train,y_train)
    P=nb.predict(X_test)
    return erreur2(P,y_test)

from sklearn.tree import DecisionTreeClassifier
nb=DecisionTreeClassifier(random_state=0)

from sklearn.neighbors import KNeighborsClassifier
nb1=KNeighborsClassifier(n_neighbors=41)

from sklearn.ensemble import RandomForestClassifier
nb2=RandomForestClassifier(n_estimators=20, max_depth=4, bootstrap=True, random_state=0)

from sklearn.naive_bayes import GaussianNB
nb3=GaussianNB()

def errorRange(id_algorithm):
    if(id_algorithm==0):
        return test(nb)
    if (id_algorithm == 1):
        return test(nb2)
    if (id_algorithm == 2):
        return test(nb3)
    if (id_algorithm == 3):
        return test(nb1)



