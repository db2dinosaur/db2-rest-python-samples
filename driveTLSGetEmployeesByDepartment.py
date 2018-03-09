import requests
import base64
import json
import sys
baseurl = 'https://s0w1.zpdt.local:2052'
url = baseurl + '/services/GILLJSRV/GetEmployeesByDepartment'
data = {
  'dept':'A00',
  'mgr':'000010'
}
# using json=xxx get us the Conten-Type: application/json header for free.
response = requests.post(url,
			 json=data,
			 verify='.\certs\zpdtca.pem',
			 cert=('.\certs\zpdt_webclient.cert.pem',
			       '.\certs\zpdt_webclient.keys.pem'))
print('Status code = ',response.status_code)
print('Returned headers:')
for name in response.headers:
	print('   ',name,': ',response.headers[name])
print('Returned data:')
json.dump(response.json(),sys.stdout,sort_keys=False,indent=4);