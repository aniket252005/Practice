#### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
import numpy as np


Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)