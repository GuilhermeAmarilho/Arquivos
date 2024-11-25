import requests

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

r.status_code
# caso retorne 200 é por que conseguiu

r.headers['content-type']
# 'application/json; charset=utf8'

r.encoding
# 'utf-8'

r.text
# '{"authenticated": true, ...'

r.json()
# {'authenticated': True, ...}