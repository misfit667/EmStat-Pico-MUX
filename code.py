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


'''DATA IMPORT'''
path = 'C:/Users/SLinf/Documents/GitHub/multiplexer-of-madness/'
file = 'data.csv'
# Opens the file into a Pandas dataframe
df = pd.read_csv(path + file, sep = ',', header = 5, encoding = "utf16", low_memory = False)
# Removes any null values from the dataframe
ndf = df.dropna()
# Converts the dataframe into an array
array = ndf.to_numpy().astype(float)
# Supresses an error in the use of np.log()
np.seterr(divide = 'ignore')


'''FILE INFORMATION'''
rows = array.shape[0]
channels = 16
fields = 4
length = array.shape[1]
experiments = length // (channels*fields)


'''DATA PROCESSING'''
# Convert the 2D array given by excel into a 4D array: (channel, experiment, dataset, data)
# Note: Managed to make a 4D array, but data was placed incorrectly during reshape
# Still need to finish this, but for now, split the 2D array into 64 columns of 2D arrays and then reshaped
for i in range(1, channels + 1): #(1-16)123456789101112131415
    FET = i - 1
    regression_data = np.empty((experiments, fields, rows))
    actual_regression_data = np.empty((experiments, 2, 250))
    for j in range(1, experiments + 1): #(1-9) 123456789

        x_source = array[ : , ((64 * j) - 64 +  + (4 * FET))]
        y_source = np.log10(np.absolute(array[ : , ((64 * j) - 63 + (4 * FET))]))
        x_drain = array[ : , ((64 * j) - 62 + (4 * FET))]
        y_drain = np.log10(np.absolute(array[ : , ((64 * j) - 61 + (4 * FET))]))

        smooth = np.convolve(y_drain, 100) / 100
        fit = piecewise_regression.Fit(x_drain, smooth, n_breakpoints = 2)
        bp1 = fit.get_results()['estimates']['breakpoint1']['estimate']
        #bp2 = fit.get_results()['estimates']['breakpoint2']['estimate']

        for item in x_drain:
            if item > bp1:
                upper = np.where(x_drain == item)
                upper_val = upper[0][0]
                break
            else:
                pass

        """ for item in x_drain:
            if item > bp2:
                lower = np.where(x_drain == item)
                lower_val = lower[0][0]
                break
            else:
                pass """

        linx = x_drain[upper_val:upper_val +250]
        liny = y_drain[upper_val:upper_val + 250]

        extraction = linregress(linx, liny)

        z = extraction[0]*linx + extraction[1]

        regression_data[j-1,0,:] = x_source
        regression_data[j-1,1,:] = y_source
        regression_data[j-1,2,:] = x_drain  
        regression_data[j-1,3,:] = y_drain  
        actual_regression_data[j-1,0,:] = linx
        actual_regression_data[j-1,1,:] = z            
                
        
    fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)

    ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
    ax.set_title('FET =' + str(i), loc = 'center', pad = 20, fontsize = 15)
    for w in range(0, experiments):
        ax.plot(regression_data[w,0,:], regression_data[w,1,:], linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None )
        ax.plot(regression_data[w,2,:], regression_data[w,3,:], linewidth = 1, linestyle = '-', color = 'red', marker = None, label = str(w+1))
        ax.plot(actual_regression_data[w,0,:], actual_regression_data[w,1,:], linewidth = 1, linestyle = '-', color = 'blue', marker = None, label = None)

    plt.legend(loc='best')
    plt.show()
    plt.close()

'''END TIME''' 
finish = (time.time() - start)
print('Time to run: ' + str(finish))