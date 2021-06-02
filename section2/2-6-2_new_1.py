#2019-01-28 수정

from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section2/food-list.html",encoding="utf-8")

soup = BeautifulSoup(fp, "html.parser")

print("1", soup.select("li:nth-of-type(4)")[1].string) #각 li 태그 그룹의 4번째 요소 선택
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string) #하나만 선택하기때문에 index필요 없음
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string) #index로 접근해야
print("4", soup.select("#ac-list > li.alcohol.high")[0].string) #class로 가져오기

param = {"data-lo": "cn", "class": "alcohol"} # dict 형태도 옵션으로 사용가
print("5", soup.find("li", param).string)
print("6", soup.find(id="ac-list").find("li",param).string)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
