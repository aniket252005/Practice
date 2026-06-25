#### 22. Normalize a 5x5 random matrix (★☆☆)
import numpy as np

Z = np.random.random((5,5))
Z = (Z - np.mean (Z)) / (np.std (Z))
print(Z)