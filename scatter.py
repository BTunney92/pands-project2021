import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

iris_data = pd.read_csv('irisdata.csv')

sns.set(style="darkgrid")

plt.title("Sepal Length & Width in cm")

sns.scatterplot(data=iris_data, x="sepal_length", y="sepal_width", hue="species") # Setting X & Y Axis labels along with hue parameter

plt.legend(bbox_to_anchor=(1.11, 1), borderaxespad=0) # Used to move the legend outside the graph. Adjust the bbox_to anchor values to move legend

plt.show() # Removed to save

plt.savefig ("Sepal Scatter.PNG")
