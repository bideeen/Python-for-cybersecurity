# import
import httplib
# create a connection 
connection = httplib.HTTPConnection('www.google.com')
# Send http rewuest
connection.request('GET','/')
# Get Response
get_response = connection.getresponse()
response_data = get_response.read()
print(response_data)
