'''MODULES'''
import time
import pandas as pd
import numpy as np
import piecewise_regression
from scipy.stats import linregress
import matplotlib.pyplot as plt
import multiplexermanager as mm
import plotting as pg
import operations as op

'''START TIME'''
# Measures the time at which the code is executed
start = time.time()     

path = 'C:/Users/SLinf/Documents/GitHub/EmStat-Pico-MUX/'
file = '20221017_1400_PBSpH7 ozoncleaner.csv'
filetwo = '20221026_1400_PBS_MUA_1.csv'
np.seterr(divide = 'ignore')

array = mm.Multiplexer(path + file).array

logged = mm.logarithm(array)
bp = op.blah(logged)
plotted = pg.compare_experiments(bp)

'''END TIME''' 
finish = (time.time() - start)
print('Time to run: ' + str(finish))



