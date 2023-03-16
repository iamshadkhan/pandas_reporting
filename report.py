import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('iris.csv')

profile = ProfileReport(df)
profile.to_file(output_file="iris.html")