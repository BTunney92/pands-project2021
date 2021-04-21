# Programming and Scripting Project 2021

# The purpose of this project is to research Fisher's Iris data set and and write code in Python to  investigate  it.

# 1) Background

Fisher's Iris data set is a multivariate data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.

The data set consists of 150 records, broken down into five traits as below;
 
  (i) Species of Iris (50 Samples each)   
     - Iris setosa, Iris virginica & Iris versicolor                 

  (ii)  Sepal width in cm

  (iii) Sepal length in cm

  (iv)  Petal width in cm

  (v)   Petal length in cm

The dataset is often used in data mining, classification and clustering examples and to test algorithms.

# 2) Libraries Used

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

Matplotlib is a low level graph plotting library in python that serves as a visualisation utility.
Pandas is used to analyse data
NumPy is a Python library used for working with arrays
Seaborn is a Python data visualisation library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

# 3) Investigation

    (i) Summary
       To carry out the initial analysis of the dataset, I used the 'Describe' function and then saved this to a text file - Summary.txt
       The describe() method is used for calculating some statistical data like percentile, mean and std of the numerical values of the Series or DataFrame
   
    (ii) Data Visualisation
        To dislay the dataset variables, I plotted four histograms showing the Sepal Length, Sepal Width, Petal Length & Petal Width -  separated by species.

        To represent the relationship between the sepal and petal variables, I plotted two scatter plots - separated by species.


     

# References

http://archive.ics.uci.edu/ml/datasets/Iris

https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

https://en.wikipedia.org/wiki/Iris_flower_data_set

http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/

https://www.w3schools.com

https://www.w3schools.com/python/python_file_open.asp

https://www.pitt.edu/~naraehan/python3/mbb12.html

https://seaborn.pydata.org/tutorial/distributions.html

https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf

https://datavizpyr.com/how-to-place-legend-outside-the-plot-with-seaborn-in-python/
