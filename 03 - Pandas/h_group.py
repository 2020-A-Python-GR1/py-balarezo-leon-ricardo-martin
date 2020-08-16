# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:56:06 2020

@author: martinb1992
"""

import pandas as pd
import math
import numpy as np

path_guardado = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

seccion_df = df.iloc[49980:50019,:].copy
