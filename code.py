'''MODULES'''
import time
import pandas as pd
import numpy as np
import piecewise_regression
from scipy.stats import linregress
import matplotlib.pyplot as plt
import multiplexermanager as mm


'''START TIME'''
# Measures the time at which the code is executed
start = time.time()     

path = 'C:/Users/SLinf/Documents/GitHub/EmStat-Pico-MUX/'
file = 'data.csv'
filetwo = 'test.csv'
np.seterr(divide = 'ignore')

array = mm.Multiplexer(path + file)
arraytwo = mm.Multiplexer(path + filetwo)

values = mm.logarithm(array)

mm.compare_experiments(values)
mm.compare_channels(arraytwo.array)

'''END TIME''' 
finish = (time.time() - start)
print('Time to run: ' + str(finish))



