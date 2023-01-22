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

#Añadir una columna
df['full_name'] = df['first'] + ' ' + df['last']

print(df)

#Borramos las columnas (inplace=True para ejecutar el cambio en el origen de datos y no en la copia en memoria)
df.drop(columns=['first','last'],inplace=True)


#Añadimos dos columnas desde una ya existente
df[['first','last']] = df['full_name'].str.split(' ', expand=True)


#Añadir una línea
newData = pd.DataFrame({'email':['email4@gmail.com'],'full_name':['John Smith'],'first':['John'],'last':['Smith']})

df = pd.concat([newData,df],ignore_index=True)

#print(df2)

#Concatenamos por fila en vez de columna
"""
temperatura = pd.DataFrame(
    {
        'ciudad':['Madrid','Barcelona','Sevilla'],
        'temperatura':[24,28,32]
    }
)

viento = pd.DataFrame(
    {
        'ciudad':['Madrid','Barcelona','Sevilla'],
        'viento':[4,18,25]
    }
)

#df2 = pd.concat([temperatura,viento],axis=1)

print(df2)
"""
#Borramos una fila, inplace para que sea permanente
#df.drop(index=3)

#filt = (df['last'] == 'Doe')
#df.drop(index=df[filt].index, inplace=True)

print (df)