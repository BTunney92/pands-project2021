# This program is designed to investigate Fishers Iris dataset
# Author: Brendan Tunney

# Importing the libraries for the program

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#Reading in the CSV dataset

iris_data = pd.read_csv('irisdata.csv')

#Using Describe() to view basic stats

Summary = iris_data.describe()

# Using Open() to create and write summary text file. 
with open("Summary.txt", "w",) as f:
     f.write(str(Summary))  #Summary must be converted to STR as dataframe will fail

f.close()  # Closing file

iris_data = pd.read_csv('irisdata.csv')

# Sepal Length using seaborn Histogram

plt.title("Sepal Length in cm") # Setting graph title

sns.displot(x="sepal_length", data=iris_data, hue = "species", multiple = "dodge") # Adding "species" value to hue creates a unique histogram colour for each species.
                                                                                   #Dodge added to make bars clearer.
    
plt.savefig ("Sepal Length Hist.PNG") # Saving picture

plt.show() # Showing the graph. Must be placed after plt.savefig to allow PNG file to save

# Sepal Width using seaborn Histogram

sns.set(style="darkgrid") # Adds background colour

sns.displot(x="sepal_width", data=iris_data, hue = "species", multiple = "dodge",)

plt.title("Sepal Width in cm") 

plt.savefig ("Sepal Width Hist.PNG")

plt.show()

# Petal Length using seaborn Histogram

sns.set(style="darkgrid") # Adds background colour

sns.displot(x="petal_length", data=iris_data, hue = "species", multiple = "dodge", binwidth = 2) # binwidth added to adjust width of bars

plt.title("Petal Length in cm")

plt.savefig ("Petal Length Hist.PNG")

plt.show() 

# Petal Width using seaborn Histogram

sns.set(style="darkgrid") 

sns.displot(x="petal_width", data=iris_data, hue = "species", multiple = "dodge", binwidth = 2) # binwidth added to adjust width of bars

plt.title("Petal Width in cm")

plt.savefig ("Petal Width Hist.PNG")

plt.show()

#Scatter Plots

#Sepal traits using seaborn scatterplot

iris_data = pd.read_csv('irisdata.csv')

sns.set(style="darkgrid")

plt.title("Sepal Length & Width in cm")

sns.scatterplot(data=iris_data, x="sepal_length", y="sepal_width", hue="species") # Setting X & Y Axis labels along with hue parameter

plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0) # Used to move the legend outside the graph. Adjust the bbox_to anchor values to move legend

plt.savefig ("Sepal Scatter.PNG")

plt.show()

# Petal traits using seaborn scatterplot

sns.set(style="darkgrid")

plt.title("Petal Length & Width in cm")

sns.scatterplot(data=iris_data, x="petal_length", y="petal_width", hue="species") # Setting X & Y Axis labels along with hue parameter

plt.legend(bbox_to_anchor=(1.11, 1), borderaxespad=0) 

plt.savefig ("Petal Scatter.PNG")

plt.show() 

# Pair Plots

sns.set(style="darkgrid")

sns.pairplot(data=iris_data, hue="species")

plt.savefig ("Pair Plot.PNG")

plt.show()



