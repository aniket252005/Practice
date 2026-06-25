#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
import numpy as np

Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)