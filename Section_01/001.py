# Using pandas, from the list below:
#
#
#     stocks = ['PLW', 'CDR', '11B', 'TEN']
#
#
# create a Series object and print it to the console.
#
#
# Expected result:
#
#
#     0    PLW
#     1    CDR
#     2    11B
#     3    TEN
#     dtype: object

import pandas as pd


stocks = ['PLW', 'CDR', '11B', 'TEN']
print(pd.Series(stocks))

