import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

from utils import helpers

path = "../data/"

df = pd.read_csv(path + "VBM_data.csv")
train, test = helpers.train_test(df)

X_train = train.loc[:, df.columns.drop(["Subjectt", "Sex", "Chr", "PD"])]
X_test = test.loc[:, df.columns.drop(["Subjectt", "Sex", "Chr", "PD"])]

y_train = train.pop("PD")
y_test = test.pop("PD")

for column in X_train.columns:
    if X_train[column].dtype == "object":
        X_train[column] = X_train[column].apply(lambda x: str(x.replace(",", "")))
        X_train[column] = X_train[column].astype("float")

for column in X_test.columns:
    if X_test[column].dtype == "object":
        X_test[column] = X_test[column].apply(lambda x: str(x.replace(",", "")))
        X_test[column] = X_test[column].astype("float")

clf = RandomForestClassifier(n_estimators=500)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
