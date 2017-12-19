import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = pd.read_csv('foo.csv')
y = pd.read_csv('y.csv')
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x.iloc[:,0],x.iloc[:,1],y,s=1)
ax.set_xlabel('SVD Component 1')
ax.set_ylabel('SVD Component 2')
ax.set_zlabel('Price (USD)')
plt.show()
