# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:47:58 2022

@author: krzys
"""
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats.stats import pearsonr  
import numpy as np


path = r'C:\Users\krzys\Desktop\data science\IV semestr\machine_learning\warm_up_excercise'
os.chdir(path)

try:
    os.mkdir(os.path.join(path, "plots"))
    os.mkdir(os.path.join(path, "csv"))
except FileExistsError:
    pass

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]


list_y = [y1, y2, y3, y4]
list_x = [x, x4]

datasetscsv = {}
datasets = {}


df = pd.DataFrame()
df_main = pd.DataFrame()

n = 0    
for x in list_x:
    for y in list_y:
        datasetscsv[n] = {'std_y' : round(np.std(y), 2),
                       'var_y' : round (np.var(y), 2),
                       'mean_y' : round (np.mean(y), 2),
                       'corr' : round (pearsonr(x, y)[0], 2),
                       'x' : str (x),
                       'y' : str(y)} 
        datasets[n] = {'std_y' : round(np.std(y), 2),
                       'var_y' : round (np.var(y), 2),
                       'mean_y' : round (np.mean(y), 2),
                       'corr' : round (pearsonr(x, y)[0], 2),
                       'x' : x,
                       'y' : y} 
        df = pd.DataFrame(data = datasetscsv[n], index=[n])
        df_main = pd.concat([df_main, df])
        df_main.to_csv('csv\data_stats.csv', index = False)
        n += 1

fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(8, 6),
                        gridspec_kw={'wspace': 0.08, 'hspace': 0.20})
axs[0, 0].scatter(datasets[0]['x'], datasets[0]['y'])
axs[0, 0].set_title("Axis [0, 0]")
axs[0, 1].scatter(datasets[1]['x'], datasets[1]['y'])
axs[0, 1].set_title("Axis [0, 1]")
axs[1, 0].scatter(datasets[2]['x'], datasets[2]['y'])
axs[1, 0].set_title("Axis [1, 0]")
axs[1, 1].scatter(datasets[3]['x'], datasets[3]['y'])
axs[1, 1].set_title("Axis [1, 1]")

for ax in axs.flat:
    ax.label_outer()
    stats = (f'$\\mu$ = {np.mean(y):.2f}\n'
             f'$\\sigma$ = {np.std(y):.2f}\n'
             f'$r$ = {np.corrcoef(x, y)[0][1]:.2f}')
    bbox = dict(boxstyle='round', fc='blanchedalmond', ec='orange')
    ax.text(0.95, 0.07, stats, fontsize=9, bbox=bbox,
            transform=ax.transAxes, horizontalalignment='right')
    
fig.savefig('plots\scatter.jpg')
