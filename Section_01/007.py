# The following quotations Series is given:
#
#
#     stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
#     quotations = pd.Series(data=stocks)
#
#
# Add two elements to this Series:
#
#     key: 'BBT', value: 25.5
#
#     key: 'F51', value: 19.2
#
# In response, print quotations Series to the console.
#
#
# Expected result:
#
#
#     PLW    387.0
#     CDR    339.5
#     TEN    349.5
#     11B    391.0
#     BBT     25.5
#     F51     19.2
#     dtype: float64

import pandas as pd


stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(data=stocks)

stocks2 =  pd.Series([25.5,19.2], index = ['BBT','F51'])
quotations = quotations.append(stocks2)
print(quotations)