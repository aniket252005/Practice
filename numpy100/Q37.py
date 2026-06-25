#### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
import numpy as np

Z = np.zeros((5,5))
Z += np.arange(5)
print(Z)