# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 07:28:27 2020

@author: martinb1992
"""


import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)

series_b = pd.Series(tupla_numeros)

series_c = pd.Series(np_numeros)

series_d = pd.Series(
    [True,
    False,
    12,
    12.12,
    "Martin",
    None,
    (1),
    [2],
    {"nombre":"Martin"}
    ])


#print(series_d[3])


lista_ciudades = [
    "Ambato",
    "Cuenca",
    "Loja",
    "Quito"
    ]

serie_ciudad = pd.Series(
    lista_ciudades,
    index = [
        "A",
        "C",
        "L",
        "Q"
        ]
    )

#print(serie_ciudad[3])
#print(serie_ciudad["C"])


valores_ciudades = {
    "Ibarra":9500,
    "Guyaquil":10000,
    "Cuenca":7000,
    "Quito":8000,
    "Loja":3000,
    }

serie_valor_ciudad = pd.Series(valores_ciudades)

ciudad_menor_5k = serie_valor_ciudad < 5000


print(type(serie_valor_ciudad))
print(type(ciudad_menor_5k))
print(ciudad_menor_5k)

s5 = serie_valor_ciudad[ciudad_menor_5k]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

svc_cuadrado = np.square(serie_valor_ciudad)


ciudades_uno = pd.Series({
    "Montañita":300,
    "Guayaquil": 10000,
    "Quito": 2000})

ciudades_dos = pd.Series({
    "Loja":300,
    "Guayaquil": 10000})


ciudades_uno["Loja"] = 0

print(ciudades_uno + ciudades_dos)

ciudades_add = ciudades_uno.add(ciudades_dos)

ciudades_concat = pd.concat([
    ciudades_dos,
    ciudades_dos])

ciudades_concat_verify = pd.concat([
    ciudades_dos,
    ciudades_dos], verify_integrity = False)



ciudades_append_verify = ciudades_uno.append(ciudades_dos, verify_integrity = False)



print(ciudades_uno.max())
print(ciudades_uno.min())

print("////")

print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))

print("head 2")

print(ciudades_uno.head(2))
print("tail 2")
print(ciudades_uno.tail(2))

def calcular(valor_serie):
    if (valor_serie <= 1000):
        return valor_serie *1.05
    if (valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie *1.10
    if (valor_serie > 5000):
        return valor_serie *1.15

print("Def Calcular")
ciudad_calculada = ciudades_uno.map(calcular)
print(ciudad_calculada)

# if Else
# cuando NO CUMPLE condicion, aplica

resultado = ciudades_uno.where(ciudades_uno < 1000, ciudades_uno * 1.05)

# CAST

print("///////////cast")

series_numeros = pd.Series(['1.0', '2', -3])

print(pd.to_numeric(series_numeros, downcast='integer'))

series_numeros_err = pd.Series(['no tiene', '1.0', '2', -3])

print(pd.to_numeric(series_numeros_err, errors='ignore'))
print(pd.to_numeric(series_numeros_err, errors='coerce'))














