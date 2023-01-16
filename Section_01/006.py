# The following Series is given:
#
#
#     series = pd.Series(['001', '002', '003', '004'], list('abcd'))
#
#
# Convert its type to int and print this Series to the console.
#
#
# Expected result:
#
#
#     a    1
#     b    2
#     c    3
#     d    4
#     dtype: int64
#
#

import pandas as pd


series = pd.Series(['001', '002', '003', '004'], list('abcd'))

print(series.astype('int'))