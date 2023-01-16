# Convert the following quotations Series:
#
#
#     stocks = {
#         'PLW': 387.00,
#         'CDR': 339.5,
#         'TEN': 349.5,
#         '11B': 391.0,
#         'BBT': 25.5,
#         'F51': 19.2
#     }
#     quotations = pd.Series(data=stocks)
#
#
# to DataFrame. Reset the index and name the columns 'ticker' and 'price' respectively.
#
# In response, print this DataFrame to the console.
#
#
# Expected result:
#
#
#       ticker  price
#     0    PLW  387.0
#     1    CDR  339.5
#     2    TEN  349.5
#     3    11B  391.0
#     4    BBT   25.5
#     5    F51   19.2

import pandas as pd


stocks = {
    'PLW': 387.00,
    'CDR': 339.5,
    'TEN': 349.5,
    '11B': 391.0,
    'BBT': 25.5,
    'F51': 19.2
}
quotations = pd.Series(data=stocks)

df = pd.DataFrame(quotations)
df.reset_index(inplace=True)
df.columns =  ['ticker','price']
print(df)

