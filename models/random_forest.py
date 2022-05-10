import pandas as pd
import sklearn
from numpy import float16, mean, std
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import (
    KFold,
    RepeatedStratifiedKFold,
    cross_val_score,
    train_test_split,
)

path = "../data/"

df = pd.read_csv(path + "VBM_data.csv")
X = df.loc[:, df.columns.drop(["Subjectt", "Sex", "Chr", "PD"])]

y = df.pop("PD")

for column in X.columns:
    if X[column].dtype == "object":
        X[column] = X[column].apply(lambda x: str(x.replace(",", "")))
        X[column] = X[column].astype("float")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = RandomForestClassifier(n_estimators=500)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
