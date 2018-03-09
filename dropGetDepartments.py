import base64
import requests
import json
import sys

# Define the Url, Headers and Body
url = 'http://s0w1.zpdt.local:2050/services/DB2ServiceManager'
data = {
  'requestType':'dropService',
  'collectionID':'GILLJSRV',
  'serviceName':'GetDepartments'
}
body = json.dumps(data)
# Define authentication details
authstr = 'Basic ' + base64.b64encode(b'MYUSER:xxxxxxxx').decode()
reqhdrs = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization':authstr
}
#Make the call 
response = requests.post(url,data=body,headers=reqhdrs)

print('Status code = ',response.status_code)
print('Returned headers:')
for name in response.headers:
        print('   ',name,': ',response.headers[name])
print('Returned data:')
json.dump(response.json(),sys.stdout,sort_keys=False,indent=4);