import pandas as pd

#Cargamos los datos desde un csv
#df = pd.read_csv('../Datos/survey-2022/data.csv')
#schema_df = pd.read_csv('../Datos/survey-2022/data_schema.csv')

people={
    "first":["Corey", "Jane", "John","Adam"],
    "last":["Schafer","Doe", "Doe","Doe"],
    "email":["email@gmail.com", "email2@gmail.com", "email3@gmail.com","email4@gmail.com"]
}

df = pd.DataFrame(people)

#podemos utilizar inplace=True para dejar el orden como definitivo
#ordenamos por una columna
#print(df.sort_values(by='last'))

#ordenamos por una columna, descendente
#print(df.sort_values(by='last',ascending=False))


#ordenamos por varias columnas, descendente
#print(df.sort_values(by=['last','first'],ascending=[False,True]))

#ordemanos via indide
#print(df.sort_index())

#ordenamos solo una columna
print(df['last'].sort_values())

#print(df)