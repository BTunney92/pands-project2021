import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

iris_data = pd.read_csv('irisdata.csv')

sns.set(style="darkgrid")

sns.pairplot(data=iris_data, hue="species")

plt.show()