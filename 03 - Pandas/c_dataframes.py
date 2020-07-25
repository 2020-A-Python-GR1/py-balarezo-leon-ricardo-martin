# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:47:00 2020

@author: martinb1992
"""


# c_dataframes.py

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

#crear el Dataframe
df1 = pd.DataFrame(arr_pand)

s1 = df1[0]

s2 = df1[1]

s3 = df1[2]

#añadir valores al dataframe

df1[3] = s1

df1[4] = s1 * s2


datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)']
    
    )

datos_fisicos_dos = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'],
    index = [
        'Martin',
        'Ricardo'
        ]
    )




#seleccionar una serie específica

print("#################")

serie_peso = datos_fisicos_dos['Peso (kg)']
datos_martin = serie_peso['Martin']

print(serie_peso)
print(datos_martin)


df1.index = ['Martin', 'Ricardo']
df1.index = ['Emily', 'Francis']

df1.columns = ['A','B','C','D','E']


















