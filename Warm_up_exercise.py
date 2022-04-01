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
from typing import List


path = r"C:\Users\krzys\Desktop\data science\IV semestr\machine_learning\machine_learning_introduction"
os.chdir(path)

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

list_y = [y1, y2, y3, y4]
list_x = [x, x4]


def main():

    datasetscsv = {}
    datasets = {}

    def stat_data(
        x_axis: List[float] or List[int], y_axis: List[float] or List[int], save=False
    ) -> dict:
        """
        Function takes arguments for x_axis and y_axis as list of ints or floats,
        calculates: 1) std, 2) var, 3) mean for y, 4) corr for x and y and saves
        it as csv in path in separate folder.
        Argument save: if True dataset will be saved as csv.
        Also returns dict with the same values as saved to csv.
        """

        if type(x_axis) != list or type(y_axis) != list:
            raise TypeError("arguments must be lists of ints or floats")
        try:
            os.mkdir(os.path.join(path, "csv"))
        except FileExistsError:
            pass
        df = pd.DataFrame()
        df_main = pd.DataFrame()

        n = 0
        for x in x_axis:
            for y in y_axis:
                datasetscsv[n] = {
                    "std_y": round(np.std(y), 2),
                    "var_y": round(np.var(y), 2),
                    "mean_y": round(np.mean(y), 2),
                    "corr": round(pearsonr(x, y)[0], 2),
                    "x": str(x),
                    "y": str(y),
                }
                df = pd.DataFrame(data=datasetscsv[n], index=[n])
                df_main = pd.concat([df_main, df])
                if save == True:
                    df_main.to_csv("csv\data_stats.csv", index=False)
                n += 1
        n = 0
        for i in datasetscsv.items():
            datasetscsv[n]["x"] = datasetscsv[n]["x"].replace("[", "").replace("]", "")
            datasetscsv[n]["y"] = datasetscsv[n]["y"].replace("[", "").replace("]", "")
            datasetscsv[n]["x"] = list(map(float, datasetscsv[n]["x"].split(",")))
            datasetscsv[n]["y"] = list(map(float, datasetscsv[n]["y"].split(",")))
            n = n + 1
        return datasetscsv


    def scatter_plots(
        x_axis: List[float] or List[int], y_axis: List[float] or List[int]
    ) -> plt:
        """
        Function takes arguments for x_axis and y_axis as list of ints or floats,
        calculates: 1) std, 2) var, 3) mean for y, 4) corr and puts it on plots.
        """

        datasets = stat_data(x_axis, y_axis)

        try:
            os.mkdir(os.path.join(path, "plots"))
        except FileExistsError:
            pass
        fig, axs = plt.subplots(
            len (x_axis),
            len (y_axis),
            sharex=True,
            sharey=True,
            figsize=((len (x_axis) * len (y_axis))*2, len (x_axis) * len (y_axis)),
            gridspec_kw={"wspace": 0.08, "hspace": 0.20},
        )
        
        # for i in range (0, len (x_axis) * len (y_axis)):
        # x_axis_number = len (x_axis)
        # y_axis_number = len (y_axis)
        # for x in x_axis_number:
        #     for y in y_axis_number:
        axs[0, 0].scatter(datasets[0]["x"], datasets[0]["y"])
        axs[0, 0].set_title("Axis [0, 0]")
        axs[0, 1].scatter(datasets[1]["x"], datasets[1]["y"])
        axs[0, 1].set_title("Axis [0, 1]")            
        axs[0, 2].scatter(datasets[2]["x"], datasets[2]["y"])
        axs[0, 2].set_title("Axis [0, 2]")
        axs[0, 3].scatter(datasets[3]["x"], datasets[3]["y"])
        axs[0, 3].set_title("Axis [0, 3]")
        axs[1, 0].scatter(datasets[4]["x"], datasets[4]["y"])
        axs[1, 0].set_title("Axis [1, 0]")
        axs[1, 1].scatter(datasets[5]["x"], datasets[5]["y"])
        axs[1, 1].set_title("Axis [1, 1]")
        axs[1, 2].scatter(datasets[6]["x"], datasets[6]["y"])
        axs[1, 2].set_title("Axis [1, 2]")
        axs[1, 3].scatter(datasets[7]["x"], datasets[7]["y"])
        axs[1, 3].set_title("Axis [1, 3]")

        n = 0
        for ax in axs.flat:
            ax.label_outer()
            stats = (
                f"$\\mu$ = {np.mean(datasets[n]['y']):.2f}\n"
                f"$\\sigma$ = {np.std(datasets[n]['y']):.2f}\n"
                f"$r$ = {np.corrcoef(datasets[n]['x'], datasets[n]['y'])[0][1]:.2f}"
            )
            bbox = dict(boxstyle="round", fc="blanchedalmond", ec="orange")
            ax.text(
                0.95,
                0.07,
                stats,
                fontsize=9,
                bbox=bbox,
                transform=ax.transAxes,
                horizontalalignment="right",
            )
            n += 1
        fig.savefig("plots\scatter.jpg")

    scatter_plots(list_x, list_y)


if __name__ == "__main__":
    main()
    