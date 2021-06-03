# 2019-01-28 수정
# 기존 daum 주식 사이트 : ajax 방식으로 변경으로 인해 이를 반영한 코드를 수정.
# pip install fake-useragent 설치 후 실행 가능

import io
import json
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Fake Header 정보
userAgent = UserAgent()


# 헤더 선언
headers = {
    'User-Agent': userAgent.chrome,
    'referer': 'https://finance.daum.net/'
}

# 다음 주식 요청 URL
sampleUrl = "https://finance.daum.net"
sampleRes = BeautifulSoup(urlopen(sampleUrl).read(), 'html.parser')


url = "https://finance.daum.net/api/domestic/trend/market_capitalization/?pagination=true&perPage=5&order=desc"

# print(request.get_method())   #Post or Get 확인
# print(request.get_full_url()) #요청 Full Url 확인

# 요청
response = urlopen(Request(url, headers=headers)).read().decode('utf-8')
soup = BeautifulSoup(response, 'html.parser')
rank_json = json.loads(response)['KOSPI'] # data -> KOSPI

# 응답 데이터 확인(Json Data)
print('res', rank_json)

# 응답 데이터 str -> json 변환 및 data 값 저장
# rank_json = json.loads(response)['data']

# 중간 확인
print('중간 확인 : ', rank_json, '\n')

for elm in rank_json:
    # print(type(elm)) #Type 확인
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']), )
