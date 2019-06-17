# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 08:16:40 2019

@author: OLENA SAIENKO
"""

import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool, WheelZoomTool
import numpy as np
from bokeh.io import show, output_file
from bokeh.plotting import figure


data = pd.read_csv('E:\Project_work\Olena\IV2019-Task4-Saienko_Olena_original_data.csv', delimiter=',', encoding = 'utf-8')
#data1 = data['Installs'].value_counts()
data1 = data.groupby(['Installs'],axis=0).count()
data1[['App']].to_csv('E:\Project_work\Olena\IV2019-Task4-Saienko_Olena_modified_data.csv',index='False', sep=',', encoding='utf-8')

data2 = pd.read_csv('E:\Project_work\Olena\IV2019-Task4-Saienko_Olena_modified_data.csv', delimiter=',', encoding = 'utf-8')
output_file('Android_App.html')
vec = data2.to_numpy()
App = vec[:len(vec)-1,1]
Install = vec[:len(vec)-1,0]
p = figure(x_range = data2['Installs'], plot_width = 2400, plot_height = 1000,x_axis_label='Installation', y_axis_label='Number of Application')
p.vbar(x=data2['Installs'], top=data2['App'], width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.add_tools(WheelZoomTool())
show(p)
