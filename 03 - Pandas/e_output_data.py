# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:27:19 2020

@author: martinb1992
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data.pickle"


df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()


#EXCEL

path_excel = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data.xlsx"
path_excel_index = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data_indexFalse.xlsx"
path_excel_columnas = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data_columns.xlsx"


sub_df.to_excel(path_excel_index, index = False)    # se puede madnar el argumento "index = false" 

columnas = ['artist', 'title', 'year' ]
    
sub_df.to_excel(path_excel_columnas, columns =  columnas)



# multiples hojas de trabajo

path_excel_mt = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt,
                        engine='xlsxwriter') 

sub_df.to_excel(writer, sheet_name = 'Primera')    
sub_df.to_excel(writer, sheet_name = 'Segunda')    
sub_df.to_excel(writer, sheet_name = 'Tercera')    

writer.save()               











# formato condicional #



path_excel_colores = "C:/Users/marti/Documents/Phyton/Repositorios Git/repos/py-balarezo-leon-ricardo-martin/03 - Pandas/data/artwork_data_colores.xlsx"


writer = pd.ExcelWriter(path_excel_colores,
                            engine = 'xlsxwriter')

num_artistas = sub_df['artist'].value_counts()

num_artistas.to_excel(writer, sheet_name = 'Artistas')


                             
hoja_artistas = writer.sheets['Artistas']


ultima_fila = len(num_artistas.index) + 1

rango_celdas = f'B2:B{ultima_fila}'

        #### O tambien puede expresarse asi la ultima fila
        ####rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1) 
        ####

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"
    }

hoja_artistas.conditional_format(rango_celdas, formato_artistas)

writer.save()
                                                
#Formato


                                       






























