#### 30. How to find common values between two arrays? (★☆☆)
import numpy as np

Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))