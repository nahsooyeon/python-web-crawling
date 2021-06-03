import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# r = requests.get('https://api.github.com/events')
# r.raise_for_status() # 에러 발생했을 때 예외 처리
# print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name','kim',domain='httpbin.org',path='/cookies') # 실제 적용되는 쿠키 형식
#

# r = requests.get('http://httpbin.org/cookies',cookies=jar)
# r.raise_for_status()
# print(r.text)
#
# r = requests.get('https://github.com',timeout=3)
# print(r.text)

# POST방식

# r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)
# print(r.text)
#
#
payload1 = {'key1': 'value1', 'key2': 'value2'} #dict
payload2 = (('key1','value1'),('key2','value2')) #tuple: 수정 불가(상수형태)
payload3 = {'some':'nice'}
#
# r = requests.post('http://httpbin.org/post', data=payload1) #form
# print(r.text)
#
r = requests.post('http://httpbin.org/post', data=json.dumps(payload3)) #json
print(r.text)
