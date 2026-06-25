#### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
import numpy as np

Z = np.linspace(0,1,11,endpoint=False)[1:]
print(Z)