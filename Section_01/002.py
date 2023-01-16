# Using pandas, from the dictionary below:
#
#
#     stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
#
#
# create a Series object and assign it to the quotations variable. In response, print quotations variable to the console.
#
#
# Expected result:
#
#
#     PLW    387.0
#     CDR    339.5
#     TEN    349.5
#     11B    391.0
#     dtype: float64
#
#
import pandas as pd


stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}

quotations = pd.Series(stocks)

print(quotations)