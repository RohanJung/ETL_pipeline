import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 

df_projects = pd.read_csv('C:/Users/rest/Documents/python/etl/ETL_pipeline/Data/projects_data.csv',dtype=str)

df_projects=df_projects.isnull().sum()

print(df_projects)


df_population = pd.read_csv('C:/Users/rest/Documents/python/etl/ETL_pipeline/Data/population_data.csv',skiprows=4)
df_population = df_population.drop('Unnamed:62',axis=1)
print(df_population)
