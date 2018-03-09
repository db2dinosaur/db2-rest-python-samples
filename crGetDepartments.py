import base64
import requests
import json
import sys

url = 'http://s0w1.zpdt.local:2050/services/DB2ServiceManager'
data = {
  'requestType':'createService',
  'sqlStmt':'SELECT DEPTNO,'+
                   'DEPTNAME,'+
				   'MGRNO,'+
				   'ADMRDEPT '+
            'FROM DEPT '+
			'ORDER BY DEPTNO',
  'collectionID':'GILLJSRV',
  'serviceName':'GetDepartments',
  'description':'List departments ordered by DEPTNO',
  'owner':'GILLJ',
  'qualifier':'DSN81210'
}
body = json.dumps(data)
# Set request auth
authstr = 'Basic ' + base64.b64encode(b'MYUSER:xxxxxxxx').decode()
# Set request headers
reqhdrs = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization':authstr
}
# Issue the request 
response = requests.post(url,data=body,headers=reqhdrs)

print('Status code = ',response.status_code)
print('Returned headers:')
for name in response.headers:
        print('   ',name,': ',response.headers[name])
print('Returned data:')
json.dump(response.json(),sys.stdout,sort_keys=False,indent=4)
