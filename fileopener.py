'''MODULES'''
import pandas as pd
import numpy as np


class Multiplexer:
    '''Takes the .csv file from PSTrace as an input and returns a 4D array 
    with data organised by channel, experiment number, columns, and rows'''
    def __init__(self, filepath = '', bipot = True, channels = 16):

        self.filepath = filepath
        self.bipot = bipot
        self.channels = channels

      
        dataframe = pd.read_csv(self.filepath, sep = ',', header = 5, encoding = "utf16", low_memory = False)
        newdataframe = dataframe.dropna()
        array = newdataframe.to_numpy().astype(float)


        if self.bipot == True:
            fields = 4
        else:
            fields = 2
        
        rows = array.shape[0]
        experiments = array.shape[1] // (self.channels * fields)
        
        newarray = np.empty((self.channels,experiments,fields,rows))

        for x in range(0, self.channels):
            for y in range(0,experiments):
                for z in range(0,fields):
                    newarray[x,y,z,:] = array[:,(z+(experiments*y)+(fields*x))]
        
        self.array = newarray    