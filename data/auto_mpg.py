from db import get_connection
import pandas as pd

def get_data():
    conn = get_connection()

    df = pd.read_sql("SELECT * FROM auto_mpg",conn)
    
    conn.close()
    return df