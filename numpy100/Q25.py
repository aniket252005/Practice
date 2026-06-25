#### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
import numpy as np

Z = np.arange(11)
Z[(3 < Z) & (Z < 8)] *= -1
print(Z)