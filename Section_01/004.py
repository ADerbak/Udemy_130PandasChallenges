# The following Series is given (quotations variable):
#
#
#     PLW    387.0
#     CDR    339.5
#     TEN    349.5
#     11B    391.0
#     dtype: float64
#
#
# Convert the quotations to the DataFrame and set the column name to 'price'. In response, print this DataFrame to the console.
#
#
# Expected output:
#
#
#          price
#     PLW  387.0
#     CDR  339.5
#     TEN  349.5
#     11B  391.0

import pandas as pd

stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(data=stocks)
quotations = quotations.to_frame('price')
print(quotations)
