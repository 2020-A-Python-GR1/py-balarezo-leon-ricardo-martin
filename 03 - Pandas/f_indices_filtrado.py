# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:42:52 2020

@author: martinb1992
"""


import pandas as pd

path_guardado = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas)) # Numpy Array

print(artistas.size)
print(len(artistas))

blake = df['artist'] == 'Blake, William' # Serie

print(blake.value_counts())

df_blake = df[blake] # DataFrame
