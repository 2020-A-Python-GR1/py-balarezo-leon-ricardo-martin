# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:41:01 2020

@author: marti
"""

import pandas as pd
import numpy as np
import os
import xlsxwriter

#path_pickle = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.pickle"
path_pickle = r"C:\Users\marti\Documents\python\py-balarezo-leon-ricardo-martin\deber 3\data\artwork_data.pickle"

df = pd.read_pickle(path_pickle)

sub_df = df.iloc[49980:50519,:].copy()

num_artistas = sub_df["artist"].value_counts()

path_excel_grafico = r"C:\Users\marti\Documents\python\py-balarezo-leon-ricardo-martin\deber 3\data\artwork_data_grafico.xlsx"


workbook = xlsxwriter.Workbook(path_excel_grafico)
worksheet = workbook.add_worksheet()


worksheet.write_column('A1', num_artistas.index)
worksheet.write_column('B1', num_artistas)


chart = workbook.add_chart({'type': 'pie'})

chart.add_series({
    'name': 'Pie data',
    'categories': '=Sheet1!$A$1:$A$84',
    'values':     '=Sheet1!$B$1:$B$84',
})

chart.set_title({'name': 'Conteo de artistas'})

chart.set_style(10)


worksheet.insert_chart('D1', chart)


workbook.close()