import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler

cols = ["fLenght", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "FM3Long", "fM3Trans","fAlpha","fDist","class"]

df = pd.read_csv("magic04.data",names=cols)
df["class"] = (df["class"]=='g').astype(int)


train, valid, test = np.split(df.sample(frac=1),[int(0.6*len(df)),int(0.8*len(df))])

def dataset(dataframe,oversample=False):
    x = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
    ROS = RandomOverSampler()
    x,y = ROS.fit_resample(x,y)
    data = np.hstack((x,np.reshape(y,(-1,1))))
    return data, x,y

train, x_train, y_train = dataset(train,oversample=True)
valid, x_valid, y_valid = dataset(valid,oversample=True)
test, x_test, y_test = dataset(test,oversample=True)

knn_model = KNeighborsClassifier(n_neighbors=4)
knn_model.fit(x_train,y_train)
y_pred = knn_model.predict(x_test)

print(classification_report(y_test,y_pred))