import pandas as pd

#Cargamos los datos desde un csv
df = pd.read_csv('../Datos/survey-2022/data.csv',index_col='ResponseId')
schema_df = pd.read_csv('../Datos/survey-2022/data_schema.csv')

#print(df.columns)
#print(df[['Currency', 'CompTotal']])


#Creamos filtro

#Sueldos mayores de 45000 (en moneda local), que trabajen con Python.
#na=False es para controlar los errores
#filt = (df['CompTotal']> 45000 & df['LanguageHaveWorkedWith'].str.contains('Python',na=False))

#aplicamos filtro
#print(df.loc[filt, ['Country','LanguageHaveWorkedWith', 'CompTotal']])

countries = ["Spain","India"]
filtroPaises = df["Country"].isin(countries)

#Sueldos mayores de 45000, que trabajen con Python y que sean de España e India
filt = ((df['CompTotal']> 45000) & (df['LanguageHaveWorkedWith'].str.contains('Python',na=False)) & filtroPaises)

#aplicamos filtro
print(df.loc[filt, ['Country','LanguageHaveWorkedWith', 'CompTotal']])
