import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#Sepal traits using seaborn scatterplot

iris_data = pd.read_csv('irisdata.csv')

sns.set(style="darkgrid")

plt.title("Sepal Length & Width in cm")

sns.scatterplot(data=iris_data, x="sepal_length", y="sepal_width", hue="species") # Setting X & Y Axis labels along with hue parameter

plt.legend(bbox_to_anchor=(1.11, 1), borderaxespad=0) # Used to move the legend outside the graph. Adjust the bbox_to anchor values to move legend

plt.savefig ("Sepal Scatter.PNG")

plt.show()

# Petal traits using seaborn scatterplot

sns.set(style="darkgrid")

plt.title("Petal Length & Width in cm")

sns.scatterplot(data=iris_data, x="petal_length", y="petal_width", hue="species") # Setting X & Y Axis labels along with hue parameter

plt.legend(bbox_to_anchor=(1.11, 1), borderaxespad=0) 

plt.savefig ("Petal Scatter.PNG")

plt.show() 