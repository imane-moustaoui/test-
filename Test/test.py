import pandas as pd 
import numpy as np
df = pd.read_csv("data.csv")



df.isnull().sum()
print(df.isnull().sum())
