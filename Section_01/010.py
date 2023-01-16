# Convert the first column of the companies DataFrame to index. In response, print companies DataFrame to the console.
#
#
# Expected result:
#
#
#                 price   ticker
#     company                   
#     Amazon     2375.0  AMZN.US
#     Microsoft   178.6  MSFT.US
#     Facebook    179.2    FB.US

import pandas as pd


data_dict = {
    'company': ['Amazon', 'Microsoft', 'Facebook'],
    'price': [2375.00, 178.6, 179.2],
    'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']
}

companies = pd.DataFrame(data=data_dict)
companies.set_index('company',inplace=True)
print(companies)
