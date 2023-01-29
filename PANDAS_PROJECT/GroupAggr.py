import pandas as pd

#Cargamos los datos desde un csv
df = pd.read_csv('../Datos/survey-2022/data.csv',index_col='ResponseId')
schema_df = pd.read_csv('../Datos/survey-2022/data_schema.csv')


pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

#print(df.columns)

#Media de todos los valores del campo
#print(df['CompTotal'].median())

#Media de todos los campos númericos
#print(df.median())

#listado de datos estadisticos generales de los datos
#print(df.describe())

#Numero de valores distintos del campo
#print(df['Country'].value_counts())

#Ahora normalizado -> Devuelve el % 
#print(df['Country'].value_counts(normalize=True))

#Agrupamos por pais
country_grp = df.groupby(['Country'])

#Obtenemos los datos agrupados de la India
#country_grp.get_group('India')

#print(country_grp['CompTotal'].value_counts())

#Mediana de Comptotal por pais
#print(country_grp['CompTotal'].median())

#Cuenta registros por genero de Spain
#print(country_grp['Gender'].value_counts().loc['Spain'])

#% registros por genero de Spain
#print(country_grp['Gender'].value_counts(normalize=True).loc['Spain'])

#Mediana de sueldo en Spain
#print(country_grp['CompTotal'].median().loc['Spain'])

#Obtenemos los datos agregados solicitados
#print(country_grp['ConvertedCompYearly'].agg(['median','mean']))

#Obtenemos los datos agregados solicitados para un solo pais
#print(country_grp['ConvertedCompYearly'].agg(['median','mean']).loc['Canada'])

#Cuanta gente trabaja con un idioma concreto en un pais
#filt= df['Country'] == 'India'
#print(df.loc[filt]['LanguageHaveWorkedWith'].str.contains('Python').sum())

#Cuanta gente trabaja con Python por pais
#print(country_grp['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum()))

#% de desarrolladores que conocen Python
#country_responders = df['Country'].value_counts()
#country_uses_python = country_grp['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum())

#python_df = pd.concat([country_responders,country_uses_python], axis='columns', sort=False)

#python_df.rename(columns={'Country':'Responders','LanguageHaveWorkedWith':'NumKnowsPython'},inplace=True)

#python_df['PctKnowsPython'] = (python_df['NumKnowsPython'] / python_df['Responders']) * 100

#python_df.sort_values(by='PctKnowsPython', ascending=False,inplace=True)
#print(python_df)
#print(python_df.loc['Spain'])


