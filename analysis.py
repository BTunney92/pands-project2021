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

#f.close()  # Closing file

# Using Open to read in the txt file created above. Encoding added as system default is different to text file method.

with open ("Summary.txt", "rt", encoding="utf-8") as f:
     plt.figure(figsize = (10, 7))
     x = data.SepalWidth
     plt.hist(x, bins = 20, color = "green")
     plt.title("Sepal Width in cm")
     plt.xlabel("Sepal_Width_cm")
     plt.ylabel("Count")
  
     plt.show()
