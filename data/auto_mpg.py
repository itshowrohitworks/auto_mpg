from .db import get_engine
import pandas as pd

def get_data():
    engine = get_engine()

    df = pd.read_sql_query("SELECT * FROM auto_mpg",engine)

    return df