import pandas as pd
import datetime as dt

#convertimos los string en fecha en tiempo de carga
d_parser = lambda x:dt.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('../Datos/survey-2022/ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)

df.head()

#Convertimos el String de fecha en fecha
#df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d %I-%p") 

#Un solo día 
#print (df.loc[0,'Date'].day_name())

#Los días de toda la serie
#print (df['Date'].dt.day_name())

#Nueva columna con el nombre de día
#df['Day of Week'] = df['Date'].dt.day_name()

#Diferencia entre fechas. Cantidad de días que hay en el modelo
#print(df['Date'].max()  - df['Date'].min())

#Filtro por año. Pandas reconoce el año aunque este en modo string
#filt = (df['Date'] >= '2019') & (df['Date'] < '2020' )
#print(df.loc[filt])

#Filtro por año. Utilizando objetos datetime
#filt = (df['Date'] >=  pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01') )
#print(df.loc[filt])

#establecemos la columna de fecha como indice
df.set_index('Date',inplace=True)
#ahora podemos filtrar a través de ella
#print(df['2020-01':'2020-03'])

#conseguir la mediana de un valor en un perido
#print(df['2020-01':'2020-03']['Close'].median())

#Conseguir un valor para un intervalo de tiempo: D->day, W->Week, etc.
#print(df['High'].resample('D').max())

#Idem pero asignando una funcion de agregacion distinta a cada columna
print(df.resample('W').agg({'Close':'mean','High':'max', 'Low':'min', 'Volume':'sum'}))

#print(df)