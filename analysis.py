import pandas as pd
import numpy as np
import seaborn as sns

iris_data = pd.read_csv('irisdata.csv')
iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

print (iris_data)
