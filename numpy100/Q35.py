#### 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
import numpy as np

A = np.ones(3)*1
B = np.ones(3)*2
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)