import pandas as pd
import numpy as np

people={
    "first":["Corey", "Jane", "John","Adam",np.nan, None, 'NA'],
    "last":["Schafer","Doe", "Doe","Doe",np.nan, np.nan, 'Missing'],
    "email":["email@gmail.com", "email2@gmail.com", "email3@gmai0l.com",np.nan, None,"email4@gmail.com", 'Missing'],
    "age":['33','55','63','36',None, None, 'Missing']
}

df = pd.DataFrame(people)

#elimina todas las filas con nan
df.dropna()



print (df)