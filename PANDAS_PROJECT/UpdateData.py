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

#Actualizamos los nombres de todas las columnas
#df.columns = ["first_name", "last_name", "email"]

#Ponemos en mayusculas todos los nombres de columnas
#df.columns = [x.upper() for x in df.columns]

#Eliminamos los espacios de los nombres de columnas
#df.columns = df.columns.str.replace(' ', '_')

#Renombramos columnas (no todas) con inplace conseguimos que los cambios sean permanentes
#df.rename(columns={'first_name': 'first','last_name':'last'},inplace=True)

#Actualizamos valores utilizando el indice, se debe enviar datos para todas las columnas
#df.loc[2] = ["John","Smith","Johnsmith@gmail.com"]

#Actualizamos solo algunas columnas
#df.loc[2,['first','last']] = ["John", "Smith"]

#Actualizamos una columna
#df.loc[2,'last']="Smith" # tambien se podría utiilzar df.at[2,'last']="Smith"

#Actualizamos utilizando un filtro
#filt = (df['email'] == 'email@gmail.com')
#df.loc[filt, "last"] = "Smith"


#Actualizar varias filas
#df["email"] = df["email"].str.upper()

#la funcion apply aplica una funcion a todas las filas
#print(df['email'].apply(len))


#Apply con función estandar
#def upper_email(email):
#    return email.upper()

#df['email'] = df['email'].apply(upper_email)

#print (df)  

#Apply con función lambda
#df['email'] = df['email'].apply(lambda x:x.lower())

#print (df)  

#Metodo apply a todo el dataframe
#print(df.apply(len)) #muestra el número de filas con datos de cada columna

#print(df.apply(len, axis="columns")) # muestra el numero de  columnas con datos en cada fila dataframe

#Utilizamos el metodo series.min de la biblioteca de pandas
#print(df.apply(pd.Series.min))
#print(df.apply(lambda x:x.min()))


#Funcion applymap para el dataframe
#print(df.applymap(len))

#Funcion map
#print(df['first'].map({'Corey':'Chris','Jane':'Mary'}))

#Funcion replace
print(df['first'].replace({'Corey':'Chris','Jane':'Mary'}))

