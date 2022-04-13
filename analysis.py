# This is a program that will analyse the data from the Fisher Iris Data set.
# Author: Sean Elliott                                    

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# I start by importing the pands, numpy and matplotlib libraries to help 
# to organise the data. I then upload the Iris Data set to my repository.
# I imported the file from 'https://archive.ics.uci.edu/ml/datasets/iris' - This file has been downloaded
# and added to the repository for handiness.

filename = 'iris.data' 

# I open the file in read mode so that we can extrapolate the data from the data set. I ensure that the mode is set to 'rt' or 
# read text mode; to ensure no overwriting of the data within the file occurs.
with open (filename, "rt") as f: 
    data = pd.read_csv(filename)

# upon opening the file I then designate the columns of information so that they are easily readable. I found the colum headings in the original webiste description.
    cols = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Type']
    print (data)

