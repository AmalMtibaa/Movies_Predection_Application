import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

mapper={}
def PrepareDataForPredection(idAlgo,content):
    dataset1 = pd.read_csv('dataset.csv', delimiter=',')
    categorical_list = list(dataset1.columns.values)
    categorical_list.remove('class')
    newdf=dataset1.loc[:, dataset1.columns != 'class']

    line1 = []
    for key in content:
        if key=="castgrade" or key=="directorGrade" or key=="writerGrade":
            if(content[key]=="Bad"):
                line1.append(0)
            if (content[key] == "Average"):
                line1.append(1)
            if (content[key] == "Good"):
                line1.append(2)
        else:
            line1.append(content[key])

    a = np.array(line1)
    df1 = pd.DataFrame(a.reshape(-1, len(a)), columns=categorical_list)
    df_concat = pd.DataFrame(pd.concat([newdf, df1]))
    df_concat.fillna(0, inplace=True)
    encoded_df = pd.DataFrame(columns=categorical_list)
    # Converting Categorical Data to integer labels
    for x1 in categorical_list:
        mapper[x1] = preprocessing.LabelEncoder()
    for x1 in categorical_list:
        if (df_concat.dtypes[x1] == object):
            encoded_df[x1] = mapper[x1].fit_transform(df_concat.__getattr__(x1).astype(str))
        else:
            encoded_df[x1] = df_concat.__getattr__(x1)

    le = preprocessing.LabelEncoder()
    myclass = le.fit_transform(dataset1.__getattr__('class'))
    if(idAlgo==0):
        nb = DecisionTreeClassifier(random_state=0)
    if (idAlgo == 1):
        nb = KNeighborsClassifier(n_neighbors=40)
    if(idAlgo==2):
        nb=RandomForestClassifier()
    if (idAlgo == 3):
        nb = GaussianNB()

    nb.fit(encoded_df[:len(encoded_df)-1],myclass)
    P=nb.predict(encoded_df[len(encoded_df)-1:])
    return P

