'''MODULES'''
import time
import pandas as pd
import numpy as np
#import piecewise_regression
from scipy.stats import linregress
import matplotlib.pyplot as plt
import multiplexermanager as mm
import fileopener as fo
import plotting as pg

'''START TIME'''
# Measures the time at which the code is executed
start = time.time()     

path = 'C:/Users/SLinf/Documents/GitHub/EmStat-Pico-MUX/'
file = 'data.csv'

np.seterr(divide = 'ignore')

array = fo.Multiplexer(path + file)

def logarithm(input):
    working = input.array
    output = np.empty((working.shape))
    for x in range(0,working.shape[0]):
        for y in range(0,working.shape[1]):
            if input.bipot == True:
                output[x,y,0,:] = working[x,y,0,:]
                output[x,y,1,:] = np.log10(np.absolute(working[x,y,1,:]))
                output[x,y,2,:] = working[x,y,2,:]
                output[x,y,3,:] = np.log10(np.absolute(working[x,y,3,:]))

            else:
                output[x,y,0,:] = working[x,y,0,:]
                output[x,y,1,:] = np.log10(np.absolute(working[x,y,1,:]))
    return output

values = logarithm(array)
pg.compare_channels(array.array)

'''END TIME''' 
finish = (time.time() - start)
print('Time to run: ' + str(finish))