# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:06:21 2020

@author: martinb1992
"""


import numpy as np
# 1) Examen

## 2) Crear un vector de ceros de tamaño 10

arreglo_2 = np.zeros(10);

#print(arreglo_2)

## 3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1

arreglo_3 = np.zeros(10)
arreglo_3[4] = 5

#print(arreglo_3)

## 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.

arreglo_4 = np.arange(50)[::-1]

## 5) Crear una matriz de 3 x 3 con valores del cero al 8

arreglo_5 = np.arange(9).reshape(3,3)

## 6) Encontrar los indices que no sean cero en un arreglo

#arreglo_6 = np.random.randint(0,10,size=(10)) #np.random.randint(0,2)

arreglo = [1,2,0,0,4,0]
arreglo_6 = np.array(arreglo)

print("los indices son: ",np.where(arreglo_6 != 0))


## 7) Crear una matriz de identidad 3 x 3 
    
arreglo_7 = np.eye(3)

## 8) Crear una matriz 3 x 3 x 3 con valores randomicos

arreglo_8 = np.random.rand(3,3,3)

## 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor

arreglo_9 = np.random.randint(1,40,size=(10,10))

print(f"el valor maximo es : {arreglo_9.max()}")
print(f"el valor minimo es : {arreglo_9.min()}")


## 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)


## 11) ¿Como crear una serie de una lista, diccionario o arreglo?
print("ejercicio 11")
#```python
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
#```


import pandas as pd



serie_lista = pd.Series(mylist)
print(serie_lista)
serie_dicionario = pd.Series(mydict)
print(serie_dicionario)
serie_arreglo = pd.Series(myarr)
print(serie_arreglo)

## 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?
print("ejercicio 12")
#```python
mylist2 = list('abcedfghijklmnopqrstuvwxyz')
myarr2 = np.arange(26)
mydict2 = dict(zip(mylist2, myarr2))
ser = pd.Series(mydict2) 

# Transformar la serie en dataframe y hacer una columna indice



ejercicio_12 = pd.DataFrame(ser).reset_index().set_index(myarr)
ejercicio_12



## 13) ¿Como combinar varias series para hacer un DataFrame?
print("ejercicio 13")
#python
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
#```

dataframe1 = pd.DataFrame(ser1)
dataframe1[1] = ser2
dataframe1

dataframe2 = pd.DataFrame(dict(serie1=ser1, serie2=ser2))
dataframe2


## 14) ¿Como obtener los items que esten en una serie A y no en una serie B?
print("ejercicio 14")

#```python
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
#```

ejercicio_14 = set(ser1) - set(ser2)


## 15) ¿Como obtener los items que no son comunes en una serie A y serie B?
print("ejercicio 15")
#```python
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
#```

ejercicio_15 = ser1.append(ser2).drop_duplicates(keep=False)


## 16) ¿Como obtener el numero de veces que se repite un valor en una serie?
print("ejercicio 16")
#```python
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
#``
print(ser.value_counts())


## 17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?
print("ejercicio 17")
#```python
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
#```


## 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un `shape` definido?


#```python
ser = pd.Series(np.random.randint(1, 10, 35))
#shape(7,5)
#```

serie = ser.values.reshape(7, 5)
df = pd.DataFrame(serie)
df


## 19) ¿Obtener los valores de una serie conociendo la posicion por indice?



ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u


ser[pos]

## 20) ¿Como anadir series vertical u horizontalmente a un DataFrame?



ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

   
df1 = pd.DataFrame(ser1)
df1[1] = ser2
df1


df2 = pd.DataFrame(ser1)
df2 = pd.concat([df2,ser2],axis=0)
df2





## 21)¿Obtener la media de una serie agrupada por otra serie?

#`groupby` tambien esta disponible en series.



frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64


ejercicio_20 = pd.DataFrame({"frutas": frutas, "pesos": pesos})
ejercicio_20.groupby(['frutas']).mean()



## 22)¿Como importar solo columnas especificas de un archivo csv?

#https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.
























