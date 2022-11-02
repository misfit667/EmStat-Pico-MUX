"""Modules"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as cf
import fileopener as fo


"""Font Settings"""
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'cm'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 20

'''Temp'''
path = 'C:/Users/SLinf/Documents/GitHub/EmStat-Pico-MUX/'
file = 'data.csv'

np.seterr(divide = 'ignore')

this = fo.Multiplexer(path + file)


def compare_channels(array):
    for x in range(0,array.shape[0]):    
        fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
        ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        '''for axis in ['left', 'right', 'top', 'bottom']:
            ax.spines[axis].set_visible(True)
            ax.spines[axis].set_linewidth(1.5)
            ax.spines[axis].set_color('black')'''
        for y in range(0,array.shape[1]):
                   
            ax.plot(array[x,y,0,:], array[x,y,1,:], linewidth = 2, linestyle = '-', color = 'green', marker = None, label = 'W nanoelectrode')
        """ try:
            ax.plot(array[x,:,2,:], array[x,:,3,:], linewidth = 2, linestyle = '-', color = 'red', marker = None, label = 'W nanoelectrode')
        except:
            pass
 """
        #output = 'example.png'
        #plt.savefig(output, dpi = 100, quality = 95, transparent = False)
        plt.show()
        plt.close()

testing_function = compare_channels(this.array)
def compare_experiments(array):
    for x in range(array.experiments):
        pass
    fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
    ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
    for axis in ['left', 'right', 'top', 'bottom']:
        ax.spines[axis].set_visible(True)
        ax.spines[axis].set_linewidth(1.5)
        ax.spines[axis].set_color('black')

    ax.set_axisbelow(True)
    ax_xcopy = ax.twiny()
    ax_ycopy = ax.twinx()

    ax.plot(x, y, linewidth = 2, linestyle = '-', color = 'green', marker = None, label = 'W nanoelectrode')

    ax.set_xlim(xmin = None, xmax = None, auto = True)
    ax_xcopy.set_xlim(ax.get_xlim())
    ax.set_ylim(ymin = None, ymax = None, auto = True)
    ax_ycopy.set_ylim(ax.get_ylim())

    ax.set_xlabel(r'$E\ vs.$ SMSE / V', labelpad = 15, fontsize = 25)
    ax.set_ylabel('$i$ / pA', labelpad = 15, fontsize = 25)

    ax.xaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'out', top = False)
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))

    ax.yaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'out', right = False)
    ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(10))

    ax_xcopy.xaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'in', top = True)
    ax_xcopy.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))
    ax_xcopy.set_xticklabels([])

    ax_ycopy.yaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'in', right = True)
    ax_ycopy.yaxis.set_major_locator(mpl.ticker.MultipleLocator(10))
    ax_ycopy.set_yticklabels([])

    ax.xaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'out', top = False)
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.05))

    ax.yaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'out', right = False)
    ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))

    ax_xcopy.xaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'in', top = True)
    ax_xcopy.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.05))

    ax_ycopy.yaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'in', right = True)
    ax_ycopy.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))

    ax.grid(which = 'major', axis = 'both', color = 'grey', linestyle = '--', linewidth = 0.5)

    fig.tight_layout()
    output = 'example.png'
    plt.savefig(output, dpi = 100, quality = 95, transparent = False)
    plt.show()
    plt.close()