# This is a program that will analyse the data from the Fisher Iris Data set.
# Author: Sean Elliott                                    

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

# I start by importing the pands, numpy, seaborn and matplotlib libraries to help 
# to organise the data. I then upload the Iris Data set to my repository.
# I imported the file from 'https://archive.ics.uci.edu/ml/datasets/iris' - This file has been downloaded
# and added to the repository for handiness.

filename = 'iris.data' 
columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Type'] 

# I open the file in read mode so that we can extrapolate the data from the data set. I ensure that the mode is set to 'rt' or 
# read text mode; to ensure no overwriting of the data within the file occurs.
# Upon opening the file I then designate the columns of information so that they are easily readable. This information can be found at the top of the program below filename.
# I found the column headings in the original website description.
    
with open (filename, "rt") as f: 
    data = pd.read_csv(filename, header=None, names=columns)
    print (data)
    
# I then ask the program to break the information down into more readable chunks - I do this by asking it to define the grouping (ie. the 3 different types of flower)
# so that the user of the program has the data at hand from the offset.

    print("Number of Samples available for each type: ")

# I then ask the program to count the information from the file, and using the headings ('Petal length' etc.) find the median, mean and max numbers of the information available
# This is done below by using the 'describe' function.

    print (data['Type'].value_counts())
    print(' ')
    print (data.describe())
   
# We then start by organising the data within the file to start making sense of the data. This is done below by telling the program the location of the data we wish to seperate and analyse.
# For example the iris_setosa will be found the in data file provided, under the heading of 'Type' - which the program will group information for those with the distinction 
# of 'Iris Setosa'. The data.loc function is used to allow the program to locate this 'data' within the file (iris.data).

iris_setosa = data.loc[data["Type"]=="Iris-Setosa"] 
iris_virginica = data.loc[data["Type"]=="Iris-Virginica"]
iris_versicolor = data.loc[data["Type"]=="Iris-Versicolor"] 

# I then create histograms from the 3 'data sets' above using seaborn. I have attached the links in the reference section for how to create histograms in seaborn. We use the FacetGrid class to map
# the histogram - using the hue parameter will allow us to represent any overlaps in the data. We then add the axes label the same as in matplotlib and make sure we append .add_legend to the 
# end of the code to show the legend for the different colours/flower type. The 'height' setting modifies the size of the output histogram for viewing.

sns.FacetGrid(data,hue="Type",height=5).map(sns.histplot,"Petal Length").add_legend()
sns.FacetGrid(data,hue="Type",height=5).map(sns.histplot,"Petal Width").add_legend()
sns.FacetGrid(data,hue="Type",height=5).map(sns.histplot,"Sepal Length").add_legend()
sns.FacetGrid(data,hue="Type",height=5).map(sns.histplot,"Sepal Width").add_legend()
plt.show()

iris_setosa.plot(kind = "scatter", x="Sepal Length", y="Count")
plt.show

# I then made a combination of the above to make a 'pair plot' which combines the information above from the 3 data sets and creates contrasting histogram and scatter plots.

sns.set_style("darkgrid")
sns.pairplot(data,hue="Type",height=4)
plt.show()
