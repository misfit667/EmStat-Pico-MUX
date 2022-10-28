'''MODULES'''
import pandas as pd
import numpy as np
import piecewise_regression
from scipy.stats import linregress
import matplotlib.pyplot as plt


'''Importing data to dataframe/array'''
# Open file into a Pandas dataframe
path = 'C:/Users/SLinf/Documents/GitHub/multiplexer-of-madness/'
file = 'data.csv'
df = pd.read_csv(path + file, sep = ',', header = 5, encoding = "utf16", low_memory = False)
# Remove any null values from the dataframe
ndf = df.dropna()
# Convert the dataframe to an array
array = ndf.to_numpy().astype(float)

rows = array.shape[0]
channels = 16
fields = 4
length = array.shape[1]
experiments = length // (channels*fields)

'''Changing array shape'''
# Convert the 2D array given by excel into a 4D array: (channel, experiment, dataset, data)
# Note: Managed to make a 4D array, but data was placed incorrectly during reshape
# Still need to finish this, but for now, split the 2D array into 64 columns of 2D arrays and then reshaped
for i in range(1, channels):
    FET = i - 1
    for j in range(1, experiments):

        x_source = array[ : , ((16 * j) - 16 +  + (4 * FET))]
        y_source = np.log10(np.absolute(array[ : , ((16 * j) - 15 + (4 * FET))]))
        x_drain = array[ : , ((16 * j) - 14 + (4 * FET))]
        y_drain = np.log10(np.absolute(array[ : , ((16 * j) - 13 + (4 * FET))]))

        smooth = np.convolve(y_drain, 100) / 100
        fit = piecewise_regression.Fit(x_drain, smooth, n_breakpoints = 2)
        bp1 = fit.get_results()['estimates']['breakpoint1']['estimate']
        bp2 = fit.get_results()['estimates']['breakpoint2']['estimate']

        for item in x_drain:
            if item > bp1:
                upper = np.where(x_drain == item)
                upper_val = upper[0][0]
                break
            else:
                pass

        for item in x_drain:
            if item > bp2:
                lower = np.where(x_drain == item)
                lower_val = lower[0][0]
                break
            else:
                pass



        linx = x_drain[upper_val:lower_val]
        liny = y_drain[upper_val:lower_val]


        extraction = linregress(linx, liny)

        z = extraction[0]*linx + extraction[1]
                
                
        
        fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)

        ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        ax.set_title('R =' + str(extraction[2]), loc = 'center', pad = 20, fontsize = 15)
        ax.plot(x_source, y_source, linewidth = 1, linestyle = '-', color = 'green', marker = None, label = None)
        ax.plot(x_drain, y_drain, linewidth = 1, linestyle = '-', color = 'red', marker = None, label = None)
        ax.plot(linx, z, linewidth = 2, linestyle = '-', color = 'blue', marker = None, label = None)
        plt.show()
        plt.close()
        '''with open(f' FET' + str(i) +'.txt', 'w') as file:
            file.write(str(x) + '\n')'''
