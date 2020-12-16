# requests와 bs4 패키지 사용할 거야
import requests
from bs4 import BeautifulSoup


# 데스크톱 크롬인것럼 요청 - 기기마다 뜨는 웹페이지가 다르게 생겼어요. 모바일과 데스크탑 접속할 때 모양 다르죠?
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# GET 요청이라 get 함수
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

# BeautifulSoup 형태로 조작할 수 있게 parsing
soup = BeautifulSoup(data.text, 'html.parser')

ranking = soup.select('#regularTeamRecordList_table > tr')
#print(ranking[0])

for ranking_table in ranking :
    rank = ranking_table.select_one('th > strong').text
    name = ranking_table.select_one('td.tm > div > span').text
    print(rank, name)
