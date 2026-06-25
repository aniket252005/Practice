#### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
import numpy as np


Z = np.matmul(np.ones((5, 3)), np.ones((3, 2)))
print(Z)