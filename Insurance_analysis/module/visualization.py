import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import sys

def distribution_plot(title, x, xlabel, bins=10, data=None, figsize=(10, 5), save=False, path=None):
    plt.figure(figsize=(12, 8))
    sns.set_style('whitegrid')
    plt.title(title)
    splot=sns.distplot(x, color='blue', kde=True, bins=bins, hist_kws={'alpha': 0.5})
    plt.xlabel(xlabel)
    plt.show()

def barplot(title, x, y, xlabel, ylabel, data=None, hue=None, palette=None, figsize=(10, 5), save=False, path=None):
    plt.figure(figsize=(12, 8))
    sns.set_style('whitegrid')
    plt.title(title)
    splot=sns.barplot(x=x, y=y, palette=palette, data=data, hue=hue)
    for p in splot.patches:
        splot.annotate(format(p.get_height(), '.2f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center',
                    size=15, 
                    xytext = (0, 9), 
                    textcoords = 'offset points')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def scatterplot(title, x, y, xlabel, ylabel, data=None, hue=None, palette=None, figsize=(10, 5), save=False, path=None):
    plt.figure(figsize=(12, 8))
    sns.set_style('whitegrid')
    plt.title(title)
    splot=sns.scatterplot(x=x, y=y, palette=palette, data=data, hue=hue)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

if __name__ == '__main__':
    pass