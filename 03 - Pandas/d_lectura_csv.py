# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:40 2020

@author: martinb1992
"""

import numpy as np
import pandas as pd

path = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows=10
    )

columnas = [
    'id',
    'artist',
    'title',
    'medium',
    'year',
    'acquisitionYear',
    'height',
    'width',
    'units'
    
    ]

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas,
    index_col='id')


path_guardado = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data.pickle"

df2.to_pickle(path_guardado)

df5 = pd.read_pickle(path_guardado)