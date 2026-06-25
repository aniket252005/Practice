#### 29. How to round away from zero a float array ? (★☆☆)
import numpy as np



Z = np.random.uniform(-10,+10,10)
print(np.copysign(np.ceil(np.abs(Z)), Z))
