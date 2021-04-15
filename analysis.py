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

title ="Sepal Length"

sns.displot(x="sepal_length", data=iris_data, hue = "species", multiple = "dodge") # Adding "species" value to hue creats a unique histogram for each species.
                                                                             #Dodge added to make bars clearer.
#plt.show()	# Show the plot (removed to allow PNG to save)

plt.savefig ("Sepal Length.PNG")