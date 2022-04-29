# <p align="center"> Pands Project - Iris Fisher Data Set
---
This project concerns the well-known Fisher’s Iris data set. You must research the data set and write documentation and code (in Python) to investigate it.

According to 'https://archive.ics.uci.edu/ml/datasets/iris':

"This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. ... The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other."

According to 'https://rpubs.com/AjinkyaUC/Iris_DataSet': 

"It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”.

The information that is included in the data set is as follows:

1) Sepal length in cm 
2) Sepal width in cm 
3) Petal length in cm 
4) Petal width in cm 
5) Class of flower: A) Iris Setosa, B) Iris Versicolour and C) Iris Virginica


<p align = "center">
    <img src = "https://miro.medium.com/max/1400/1*f6KbPXwksAliMIsibFyGJw.png" width = "600" title = "hover text">

**<p align="center"> Analysis of Results**

From what we can see from the dataset above - when passed through the program that I have written it has produces a range of results about the 3 species of Iris.
When comparing Sepal Length the Iris Virginica had some of the larger varieties found on the particular day that the information was collected. However the general 
sepal length of the 3 species seems to be, on average, fairly consistent (with a few irregularities here and there.) Generally in Sepal Length the majority of Iris' measured 
came between 5cm and 7cm in length, with the mean measurement coming in at 5.84cm. The same could be said for Sepal Width, with the majority of flowers coming in between 2.5cm and 3.5cm with the mean measurement being 3.05cm.

Petal Length and Width provide much starker sets of information. Iris Setosa's petal sizes, both in width and length were dwarfed by the other two species - with petal length of between 1cm and 2cm - with the average being 1.5cm and the average petal width being between 0.1cm and 0.5cm. According to the dataset provided the Iris Versicolor has longer petals starting at 3cm and finishing just over 5cm in length - with the average being 4.00cm. The petal width measurements were between 1.0cm and 1.75cm respectively in the Iris Versicolor, with an average measurement of 1.375cm.

According to the dataset the Iris Virginica has much longer and wider petals than the other two species - the average petal length ranged between 5cm and 7cm with the average being 5.5cm, while the petal width went from 1.5cm to 2.5cm - with the average being 2cm in width. Compared to the Setosa the Virginica also has longer sepal length from 5.5cm to 8cm in length. The Sepal width in the Virginica was also fairly average - spanning from 2.5cm to 3.75cm in width with the average reading being 3.0cm.

<p align = "center">
    <img src = "https://miro.medium.com/max/700/1*pVEZeY3VDFbHDIAfobT5ow.png" width = "600" title = "hover text">


**<p align="center"> Walkthrough of Program**

I found this quite a challenging program to write. It combined many aspects of the course which we had covered, but also required me to learn how to use seaborn - which I found to be an excellent tool for data visualisation and analysis. The program starts by reading in the dataset 'iris.data' and outputs a summary of the raw data to a single text file. I then go on to analyse the data in various ways using the 3 species of Iris Flower; Iris Setosa, Iris Virginica and Iris Versicolor.

Using seaborn I started by creating a histogram plot of the three species of flower, comparing sepal length, sepal width, petal length and petal width across the three species. I also then allow the program to save the histograms as .png files to the repository for viewing. I then created a distplot which combines the above histogram with a trendline running through it. I found this to be more visually appealing than just the histogram plot on it's own.

I then went on to create a scatterplot of the 3 species which would help me to compare the sepal length/sepal width and the petal length/petal width of the 3 species. There are 6 itterations/comparison scatterplots of the data which are displayed when the program is run. I included a legend with each scatterplot and made sure to correctly label the axes to avoid any confusion.

I then created a pairplot - this is a combination all of the above data - combining the scatter plots and also distplots to show all of the information in one place. I found this to be particularly appealing to look at and found that it helped give me a much wider view of the information contained within the dataset.

I decided to add a boxplot as another challenge to myself to represent the data in a different way than I would have been used to. The boxplot showed some interesting differences between the species - showing that the Iris Setosa has much smaller petals than the other two species. It also clearly shows that the iris Virginica is the larger of the three species with much larger petals and only slightly smaller sepal width.

Finally I added a jointplot which I found in the seaborn documentation. I found this combination of the scatterplot in the centre with the trendlines on the exterior a very appealing way of comparing the data - and used the program to compare Petal Length and Sepal Length.

**<p align="center"> References**

https://stackoverflow.com/questions/35415241/adding-column-names-to-csv-file-python 

https://www.analyticsvidhya.com/blog/2021/06/complete-guide-to-working-with-csv-files-in-python-with-pandas/ 

https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/

https://towardsdatascience.com/data-grouping-in-python-d64f1203f8d3 

https://www.askpython.com/python-modules/pandas/python-loc-function 

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html 

https://seaborn.pydata.org/installing.html

https://seaborn.pydata.org/generated/seaborn.histplot.html

https://seaborn.pydata.org/tutorial/aesthetics.html

https://seaborn.pydata.org/generated/seaborn.FacetGrid.html

https://www.qimacros.com/histogram-excel/how-to-determine-histogram-bin-interval/ 

https://datatofish.com/plot-histogram-python/ 

https://seaborn.pydata.org/generated/seaborn.pairplot.html  

https://www.delftstack.com/howto/seaborn/legend-seaborn-plot/

https://stackoverflow.com/questions/36018681/stop-seaborn-plotting-multiple-figures-on-top-of-one-another 

https://seaborn.pydata.org/tutorial/function_overview.html

https://www.codecademy.com/article/seaborn-design-ii 

https://www.geeksforgeeks.org/python-pandas-dataframe-corr/ 

https://seaborn.pydata.org/generated/seaborn.boxplot.html 

https://seaborn.pydata.org/tutorial/function_overview.html

https://dev.to/thalesbruno/subplotting-with-matplotlib-and-seaborn-5ei8 

https://stackoverflow.com/questions/54959764/seaborn-factorplot-generates-extra-empty-plots-below-actual-plot 

https://towardsdatascience.com/4-pandas-groupby-tricks-you-should-know-9e5b9870693e 

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html 

https://realpython.com/python-csv/ 
