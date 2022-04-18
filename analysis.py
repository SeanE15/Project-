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

    iris = pd.read_csv(filename, header=None, names=columns)

    print (iris)
    
# I then ask the program to break the information down into more readable chunks - I do this by asking it to define the grouping (ie. the 3 different types of flower)
# so that the user of the program has the data at hand from the offset.

    print("Number of Samples available for each type: ")

# I then ask the program to count the information from the file, and using the headings ('Petal length' etc.) find the median, mean and max numbers of the information available
# This is done below by using the 'describe' function.

    print (iris['Type'].value_counts())

    print(' ')

    print (iris.describe())
   
# We then start by organising the data within the file to start making sense of the data. This is done below by telling the program the location of the data we wish to seperate and analyse.
# For example the iris_setosa will be found the in data file provided, under the heading of 'Type' - which the program will group information for those with the distinction 
# of 'Iris Setosa'. The data.loc function is used to allow the program to locate this 'data' within the file (iris.data).

iris_setosa = iris.loc[iris["Type"]=="Iris-setosa"] 

iris_virginica = iris.loc[iris["Type"]=="Iris-virginica"]

iris_versicolor = iris.loc[iris["Type"]=="Iris-versicolor"] 

# I then create histograms from the 3 'data sets' above using seaborn. I have attached the links in the reference section for how to create histograms in seaborn. We use the FacetGrid class to map
# the histogram - using the hue parameter will allow us to represent any overlaps in the data. We then add the axes label the same as in matplotlib and make sure we append .add_legend to the 
# end of the code to show the legend for the different colours/flower type. The 'height' setting modifies the size of the output histogram for viewing.

#sns.FacetGrid(iris,hue="Type",height=5).map(sns.histplot,"Petal Length").add_legend()

#sns.FacetGrid(iris,hue="Type",height=5).map(sns.histplot,"Petal Width").add_legend()

#sns.FacetGrid(iris,hue="Type",height=5).map(sns.histplot,"Sepal Length").add_legend()

#sns.FacetGrid(iris,hue="Type",height=5).map(sns.histplot,"Sepal Width").add_legend()

#plt.show()

# I also wrote below a different output which looks to me more appealing that the simple hsitograms - I create a distplot instead of a histplot above. I prefer the look of the dist plot 
# and the trend line makes the plot more engaging to read (in my opinion...)

#sns.FacetGrid(iris,hue="Type",height=5).map(sns.distplot,"Petal Length").add_legend()

#sns.FacetGrid(iris,hue="Type",height=5).map(sns.distplot,"Petal Width").add_legend()

#sns.FacetGrid(iris,hue="Type",height=5).map(sns.distplot,"Sepal Length").add_legend()

#sns.FacetGrid(iris,hue="Type",height=5).map(sns.distplot,"Sepal Width").add_legend()

#plt.show()


# At this point I had to change the file name in the program from 'data' to 'iris' as it was confusing the program when it came to plotting the scatter plots (ie. could not have two itterations of 'data')
# This is shown below and throughout the program above. I also noticed that in the previous itteration of the program I had mislabeled the 'Type' with capital Letters instead of lower case.
# This had been throwing off the results of my scatter plot, once rectified the results came out correct. This hadn't been an issue previously as the information for the histograms was 
# coming from the entire 'iris' dataset instead of individual 'type' subheadings.  

palette = sns.color_palette("bright", 4)

sns.scatterplot(data = iris_setosa, x= "Sepal Length", y = "Sepal Width", style = "Type", palette = palette)

#sns.scatterplot(data = iris_virginica, x= "Sepal Length", y = "Sepal Width", style = "Type")

#sns.scatterplot(data = iris_versicolor, x= "Sepal Length", y = "Sepal Width", style = "Type")

#plt.savefig('seanelliottSLSW.png', dpi = 500)

#sns.scatterplot(data = iris_setosa, x= "Petal Length", y = "Petal Width", style = "Type")

#sns.scatterplot(data = iris_virginica, x= "Petal Length", y = "Petal Width", style = "Type")

#sns.scatterplot(data = iris_versicolor, x= "Petal Length", y = "Petal Width", style = "Type")

#plt.savefig('seanelliottPLPW.png', dpi = 500)

# I then made a combination of the above to make a 'pair plot' which combines the information above from the 3 data sets and creates contrasting histogram (with trend lines) and scatter plots.

#sns.set_style("darkgrid")

#sns.pairplot(iris,hue="Type",height=4)

#plt.show()
