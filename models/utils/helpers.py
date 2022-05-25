import math

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def train_test(data: pd.DataFrame):
    
    """Return train-test subjects"""

    pd_patients = data[:14]
    sleep_patients = data[14:]

    print(f"number of sleep patients: {len(sleep_patients)}")
    print(f"number of PD patients: {len(pd_patients)}")

    number_of_train_pd = math.floor(0.6 * len(pd_patients))  # = 8
    number_of_train_sleep = math.floor(0.6 * len(sleep_patients))  # = 14
    train_pd = pd_patients[:number_of_train_pd]
    train_sleep = sleep_patients[:number_of_train_sleep]

    test_pd = pd_patients[number_of_train_pd:]
    test_sleep = sleep_patients[number_of_train_sleep:]

    assert len(train_pd) + len(test_pd) == len(pd_patients)
    assert len(train_sleep) + len(test_sleep) == len(sleep_patients)

    train = pd.concat([train_pd, train_sleep])
    test = pd.concat([test_pd, test_sleep])

    return train, test

def drop_categorical(data: pd.DataFrame):
        
    '''Drop categorical variables + Age & PSQI'''

    categ = ['Subjectt','Sex','Chr']
    le = LabelEncoder()
    data[categ] = data[categ].apply(le.fit_transform)

    for column in data.columns:
        if data[column].dtype == "object":
            data[column] = data[column].apply(lambda x: str(x.replace(",", "")))
            data[column] =data[column].astype("float")

    X = data.loc[:, data.columns.drop(["Subjectt", "Age", "Sex", "Chr", "PD", "PSQI"])]
    
    return X





