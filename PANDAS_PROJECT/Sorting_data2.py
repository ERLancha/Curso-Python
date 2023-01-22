import pandas as pd

#Cargamos los datos desde un csv
df = pd.read_csv('../Datos/survey-2022/data.csv',index_col='ResponseId')
schema_df = pd.read_csv('../Datos/survey-2022/data_schema.csv')


pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

print(df.columns)

df.sort_values(by=['Country','CompTotal'], inplace=True)


print(df[['Country','CompTotal']].head(100))