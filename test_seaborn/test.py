import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

# Histogramas
plt.show()

datos1 = np.random.randn(100)
print(datos1)

print(plt.hist(datos1))

print(sns.distplot(datos1,color="green", alpha=0.8))

