#### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
import numpy as np

Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)