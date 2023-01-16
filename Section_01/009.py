# Create the following DataFrame object and assign it to the companies variable:
#
#
#          company   price   ticker
#     0     Amazon  2375.0  AMZN.US
#     1  Microsoft   178.6  MSFT.US
#     2   Facebook   179.2    FB.US
#
#
# In response, print companies DataFrame to the console.
#

import pandas as pd

stocks = [
    ['Amazon',2375.00,'AMZN.US'],
    ['Microsoft',178.6, 'MSFT.US'],
    ['Facebook', 179.2, 'FB.US']
]
companies = pd.DataFrame(stocks)
companies.columns =  ['company','price','ticker']
print(companies)