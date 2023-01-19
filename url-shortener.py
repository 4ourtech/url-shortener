import bitly_api
 
API_USER = "alvinja"
API_KEY = "cb20f68d127028993fac93e4853d394bddc51fe8"
bitly = bitly_api.Connection(API_USER, API_KEY)
 
response = bitly.shorten('http://google.com/')
 
# Now let us print the Bitly URL
print(response)