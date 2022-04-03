# This is a program that will analyse the data from the Fisher Iris Data set.
# Author: Sean Elliott                                    

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


filename = 'pands-project\iris.data' 
with open (filename, "rt") as f: 
    data = pd.read_csv(filename)
    cols = ['sepal length', 'sepal width', 'petal length', 'petal width']
    print (data)


