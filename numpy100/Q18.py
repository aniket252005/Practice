#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
import numpy as np

Z = np.diag(1+np.arange(4),k=-1)
print(Z)