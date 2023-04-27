#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def make_graph(dimension, save=False):
    ## Set the graph limits and tick interval
    xmin, xmax, ymin, ymax = -1*dimension, dimension, -1*dimension, dimension
    ticks_frequency = 1

    ## Make the plot figure
    fig, ax = plt.subplots(figsize=(dimension, dimension))

    ## Set scale ratios as equal
    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

    ## Set spines?
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ## Label the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

    ## Create ticks
    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    ## Draw grid lines
    ax.grid(which='both', color='gray', linewidth=1, linestyle='-', alpha=0.2)

    ## Add some arrows
    arrow_format = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_format)
    ax.plot((-1), (0), marker='<', transform=ax.get_yaxis_transform(), **arrow_format)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_format)
    ax.plot((0), (-1), marker='v', transform=ax.get_xaxis_transform(), **arrow_format)

    if save:
        plt.savefig(f'graph_{dimension}x{dimension}.png')
    else:
        plt.show()
