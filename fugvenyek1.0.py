import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 16])
ypoints = np.array([0, 25])

plt.plot(xpoints, ypoints)
plt.plot([50,50], [0,50])
plt.plot([4,4], [0,50])
plt.plot([4,50], [0,0])
plt.plot([4,50], [50,50])
plt.plot([0,50], [0,75])
plt.show()
