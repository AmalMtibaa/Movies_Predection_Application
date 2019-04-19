import pandas as pd
from sklearn import preprocessing
from itertools import cycle
import pylab as pl

#---For printing data
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


mapper={}
def PrepareData(df):
    # replace the Nan with "NA" which acts as a unique category
    df.fillna(0, inplace=True)
    # make list of all column headers
    categorical_list = list(df.columns.values)
    #exclude the class column
    categorical_list.remove('class')
    newdf = pd.DataFrame(columns=categorical_list)
    #Converting Categorical Data to integer labels
    for x in categorical_list:
        mapper[x]=preprocessing.LabelEncoder()
    for x in categorical_list:
        if (df.dtypes[x]==object):
            newdf[x]= mapper[x].fit_transform(df.__getattr__(x).astype(str))
        else:
            newdf[x]=df.__getattr__(x)
    # make a class series encoded :
    le = preprocessing.LabelEncoder()
    myclass = le.fit_transform(df.__getattr__('class'))
   #newdf is the dataframe with all columns except classcoumn and myclass is the class column
    return newdf.values, myclass , categorical_list


from sklearn.metrics import accuracy_score
dataset1 = pd.read_csv('dataset.csv',delimiter=',')
print(dataset1)
data,target,c=PrepareData(dataset1)


def plot_2D(data, target, target_names):
    colors = cycle('rgbcmykw') # cycle de couleurs
    target_ids = range(len(target_names))
    pl.figure()
    for i, c, label in zip(target_ids, colors, target_names):

        pl.scatter(data[target == i, 7], data[target == i, 8], c=c, label=label)


    pl.legend()
    pl.show()

#plot_2D(irisData.data,irisData.target,["Iris-setosa","Iris-versicolor","Iris-virginica"])
plot_2D(data,target,["flop","average","hit","super-hit","blockbuster"])