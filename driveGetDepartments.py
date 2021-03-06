import requests
import base64
import json
import sys

baseurl = 'http://s0w1.zpdt.local:2050'
url = baseurl + '/services/GILLJSRV/GetDepartments'
authstr = 'Basic ' + base64.b64encode(b'MYUSER:xxxxxxxx').decode()
reqhdrs = {
  'Authorization':authstr,
  'Content-Type':'application/json'
}
response = requests.post(url,headers=reqhdrs)

print('Status code = ',response.status_code)
print('Returned headers:')
for name in response.headers:
	print('   ',name,': ',response.headers[name])
print('Returned data:')
json.dump(response.json(),sys.stdout,sort_keys=False,indent=4);