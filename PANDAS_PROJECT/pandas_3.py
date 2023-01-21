import pandas as pd

#Cargamos los datos desde un csv
#df = pd.read_csv('../Datos/survey-2022/data.csv')
#schema_df = pd.read_csv('../Datos/survey-2022/data_schema.csv')

people={
    "first":["Corey", "Jane", "John"],
    "last":["Schafer","Doe", "Doe"],
    "email":["email@gmail.com", "email2@gmail.com", "email3@gmail.com"]
}

df = pd.DataFrame(people)

#modifica el indice y lo graba en el data set
df.set_index('email', inplace=True)

#print(df)

#Ahora podemos buscar datos por la nueva columna indice
print(df.loc['email@gmail.com'])

print(df.loc['email@gmail.com','last'])

#o buscar por indice
print(df.iloc[0])

#Volvemos a poner el indice inicial
df.reset_index(inplace=True)

