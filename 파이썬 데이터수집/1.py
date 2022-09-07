import requests
from bs4 import BeautifulSoup
import json

# iernet.kins.re.kr에서 방사선 수치 뷰티풀숲 라이브러리를 이용하여 크롤링

data = []  # json형식을 저장할 배열 선언

response = requests.get('http://iernet.kins.re.kr/if/search_list.asp?ke_flag=&sido=1&stat=')
source = response.text
soup = BeautifulSoup(source, "html.parser")
tag = soup.select('tr[id=tr_1]')  # 테이블 TR에서 서울 ID tr_1으로 찾기
seoulValue = tag[0].select('td')  # 찾은 tag에서 TD만 정리 
# print('서울', seoulValue[1].string)
a1 = {'name':'seoul','radiation':seoulValue[1].string,'rati':37.5655,'longi':126.9947}
data.append(a1)


response = requests.get('http://iernet.kins.re.kr/if/search_list.asp?ke_flag=&sido=9&stat=')
source = response.text
soup = BeautifulSoup(source, "html.parser")
tag = soup.select('tr[id=tr_11]')
seoulValue = tag[0].select('td')
# print('강릉', seoulValue[1].string)
a1 = {'name':'Gangneung','radiation':seoulValue[1].string,'rati':37.752217,'longi':128.875856}
data.append(a1)


response = requests.get('http://iernet.kins.re.kr/if/search_list.asp?ke_flag=&sido=4&stat=')
source = response.text
soup = BeautifulSoup(source, "html.parser")
tag = soup.select('tr[id=tr_4]')
seoulValue = tag[0].select('td')
# print('대전', seoulValue[1].string)
a1 = {'name':'Daejeon','radiation':seoulValue[1].string,'rati':36.350768,'longi':127.384794}
data.append(a1)


response = requests.get('http://iernet.kins.re.kr/if/search_list.asp?ke_flag=&sido=14&stat=')
source = response.text
soup = BeautifulSoup(source, "html.parser")
tag = soup.select('tr[id=tr_32]')
seoulValue = tag[0].select('td')
# print('여수', seoulValue[1].string)
a1 = {'name':'Yeosu','radiation':seoulValue[1].string,'rati':34.7531,'longi':127.749}
data.append(a1)


response = requests.get('http://iernet.kins.re.kr/if/search_list.asp?ke_flag=&sido=16&stat=')
source = response.text
soup = BeautifulSoup(source, "html.parser")
tag = soup.select('tr[id=tr_7]')
seoulValue = tag[0].select('td')
# print('제주', seoulValue[1].string)
a1 = {'name':'Jeju','radiation':seoulValue[1].string,'rati':33.3784,'longi':126.5307}
data.append(a1)


response = requests.get('http://iernet.kins.re.kr/if/search_list.asp?ke_flag=&sido=18&stat=')
source = response.text
soup = BeautifulSoup(source, "html.parser")
tag = soup.select('tr[id=tr_9205]')
seoulValue = tag[0].select('td')
# print('고리원자력발전소', seoulValue[1].string)
a1 = {'name':'Gori','radiation':seoulValue[1].string,'rati':35.3343,'longi':129.2886}
data.append(a1)

# 출력 데이터 프린트로 화면 확인
print(json.dumps(data, ensure_ascii=False, indent="\t"))

# 결과물을 radiation.json 파일로 저장
with open('radiation.json', 'w', encoding="utf-8") as make_file:
    json.dump(data, make_file, ensure_ascii=False, indent="\t")
