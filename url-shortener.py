import bitly_api as bitly
 
BITLY_ACCESS_TOKEN ="ACCESS_TOKEN"
 
b = bitly.Connection(access_token = BITLY_ACCESS_TOKEN)
 
response = b.shorten('http://google.com/')
print(response)