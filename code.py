'''MODULES'''
import time
import pandas as pd
import numpy as np
#import piecewise_regression
from scipy.stats import linregress
import matplotlib.pyplot as plt
import multiplexermanager as mm
import operations as op
import plotting as pg


'''START TIME'''
# Measures the time at which the code is executed
start = time.time()     

path = 'C:/Users/SLinf/Documents/GitHub/EmStat-Pico-MUX/'
file = 'data.csv'
filetwo = 'test.csv'
np.seterr(divide = 'ignore')

array = mm.Multiplexer(path + file).array
logged = op.logarithm(array)
#smoothed = op.smooth(logged,500)
tested = op.blah(logged)
#pg.compare_channels(tested)

fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
ax.set_title('Channel ', loc = 'center', pad = 20, fontsize = 15)
            
ax.plot(logged[0,0,0,:], logged[0,0,1,:], linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None)
ax.plot(logged[0,0,2,:], logged[0,0,3,:], linewidth = 1, linestyle = '-', color = 'red', marker = None, label = None)
ax.plot(tested[0,0,2,:], (tested[0,0,3,:]), linewidth = 1, linestyle = '-', color = 'blue', marker = None, label = None)

plt.show()
plt.close()

'''END TIME''' 
finish = (time.time() - start)
print('Time to run: ' + str(finish))



