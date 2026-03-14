# use to run script: python -m src.data_preprocessing

from data.auto_mpg import get_data
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

df = get_data()

print(df.head())