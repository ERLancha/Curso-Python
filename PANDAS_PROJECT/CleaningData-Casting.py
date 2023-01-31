import pandas as pd
import numpy as np

people={
    "first":["Corey", "Jane", "John","Adam",np.nan, None, 'NA'],
    "last":["Schafer","Doe", "Doe","Doe",np.nan, np.nan, 'Missing'],
    "email":["email@gmail.com", "email2@gmail.com", "email3@gmai0l.com",np.nan, None,"email4@gmail.com", 'Missing'],
    "age":['33','55','63','36',None, None, 'Missing']
}

df = pd.DataFrame(people)

#elimina todas las filas con nan or none
df.dropna()

#parámetros por defecto
#axis= [index, column], how=[all,any]
#df.dropna(axis='index',how='any')
#inplace=True

#eliminamos todas las filas que no tengan valores correctos en last y email
df.dropna(axis='index',how='all',subset=['last','email'])

#Cambia un valor de error personalizdo por los nan o none
df.replace('NA',np.nan,inplace=True)
df.replace('Missing',np.nan,inplace=True)

df.dropna(axis='index',how='all',subset=['last','email'])

#cambia todos los na por 0
df.fillna(0)

print (df.isna())