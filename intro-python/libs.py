# numpy
# pip install numpy

#pandas
#pip install pandas

import pandas as pd
import numpy as np

lista = [1, 2, 3, 4, 5]

np_list = np.array(lista)
np_list2 = np.array([6, 7, 8, 9, 10])

# print(lista, type(lista))
# print(np_list, type(np_list))

# print(np_list.sum())
# print(np_list.mean())
# print(np_list.dot(np_list2))

#conjunto de información
data = {
    "nombres": ['Juan', 'Edgar', 'Pedro'],
    "edades": [28, 30, 15]
}

ds = pd.DataFrame(data)

#agrega una nueva columna al DataSet
ds = ds.assign(nueva_columna = ds['edades'] * 2)

# print(ds[ ds['edades'] > 18 ])

empleados = {'nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Sofía', 'Carlos', 'Laura'],
        'edad': [28, 25, 31, 27, 30, 24, 29, 26],
        'ciudad': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Bogotá', 'Medellín', 'Cali', 'Barranquilla'],
        'salario': [2000000, 1500000, 3000000, 2500000, 3500000, 1800000, 2700000, 2200000]}

df_empleados = pd.DataFrame(empleados)

# print(df_empleados.info() ) # devuelve información sobre el DataFrame
# print(df_empleados.head()) # devuelve los primeros 5 registros del dataframe

# empleados_ordenados = df_empleados.sort_values('edad' , ascending = True  )

# print( empleados_ordenados[ empleados_ordenados['ciudad'] == 'Medellín' ] )
# print( empleados_ordenados[ empleados_ordenados.ciudad == 'Medellín' ] )

# columnas = ['nombre', 'edad']

# print( empleados_ordenados.loc[ empleados_ordenados.ciudad == 'Medellín', columnas  ])

# print(df_empleados.groupby('ciudad')['edad'].mean() )
# print(df_empleados.groupby('ciudad').edad.mean() )

# print(df_empleados.loc[ (df_empleados['ciudad'] == 'Medellín') | (df_empleados['ciudad'] == 'Bogotá') ])

print(df_empleados.loc[df_empleados['ciudad'].str.contains('Bo.*')])

