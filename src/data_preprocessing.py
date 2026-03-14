# use to run script: python -m src.data_preprocessing

from data.auto_mpg import get_data
import pandas as pd
from sklearn.impute import SimpleImputer

def preprocessing(data):

    # Dropping unwanted columns:
    data.drop(data.select_dtypes('str'),axis=1,inplace=True)

    # Handling Missing Values:
    impute = SimpleImputer(strategy="mean")
    missing_value_colm = data.columns[data.isnull().any()].tolist()
    data[missing_value_colm] = impute.fit_transform(data[missing_value_colm])

    # Input and Output features:
    X = data.drop('mpg',axis=1)
    y = data['mpg']

    return X,y