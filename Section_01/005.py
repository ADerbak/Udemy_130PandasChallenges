# Using the numpy and pandas create the following Series:
#
#
#     101    10.0
#     102    20.0
#     103    30.0
#     104    40.0
#     105    50.0
#     106    60.0
#     107    70.0
#     108    80.0
#     109    90.0
#     dtype: float64
#
#
# In response, print this Series to the console.

import numpy as np
import pandas as pd

y = pd.Series(np.arange(10.0,100.0, 10))

y.index += 101
print(y)