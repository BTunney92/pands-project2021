# This program is designed to investigate Fishers Iris dataset
# Author: Brendan Tunney


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


