#### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
import numpy as np

yesterday = np.datetime64('today') - np.timedelta64(1)
today     = np.datetime64('today')
tomorrow  = np.datetime64('today') + np.timedelta64(1)