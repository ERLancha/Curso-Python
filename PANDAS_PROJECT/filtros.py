import pandas as pd

#Cargamos los datos desde un csv
df = pd.read_csv('../Datos/survey-2022/data.csv',index_col='ResponseId')
schema_df = pd.read_csv('../Datos/survey-2022/data_schema.csv')

#print(df.columns)
print(df[['Currency', 'CompTotal']])