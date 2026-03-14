# use to run script: python -m src.data_preprocessing

from data.auto_mpg import get_data
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = get_data()
def preprocessing(data):

    # Dropping unwanted columns:
    data.drop(df.select_dtypes('str'),axis=1,inplace=True)

    # Handling Missing Values:
    impute = SimpleImputer(strategy="mean")
    missing_value_colm = df.columns[df.isnull().any()].tolist()
    df[missing_value_colm] = impute.fit_transform(df[missing_value_colm])

    # Input and Output features:
    X = df.drop('mpg',axis=1)
    y = df['mpg']

    return X,y