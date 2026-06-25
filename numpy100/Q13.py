#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)

import numpy as np

Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)
