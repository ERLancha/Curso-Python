import pandas as pd

#Cargamos los datos desde un csv
df = pd.read_csv('../Datos/survey-2022/data.csv',index_col='ResponseId')
schema_df = pd.read_csv('../Datos/survey-2022/data_schema.csv')

# mostramos los primeros registros
#print(df.head())

#configuramos la salida que se muestra
#pd.set_option('display.max_columns',79)
#pd.set_option('display.max_rows',79)


# mostramos los ultimos registros
#print(df.tail(50))

# recuperamos las dos primeras filas completas
#print(df.iloc[2])

# recuperamos las filas 2 y 9 columnas 2 a 6
#print(df.iloc[[2,9],2:6])

# recuperamos cuantas filas y columnas tiene el dataset
#print (df.shape)

# recuperamos la lista de columnas
#print (df.columns)

# recuperamos una columna completa
#print(df['Employment'])

# recuperamos las filas 0 y 1 y las columnas por nombre
#print(df.loc[[0,1],['Employment', 'EdLevel']])

# contamos los distintos valores de una columna
#print(df['EdLevel'].value_counts())

print(df.loc[[1,2],'Employment'])
print(df.loc[0:2,'Employment':'YearsCode'])