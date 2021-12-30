import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient #파이몽고를 쓰겠다
client = MongoClient('localhost', 27017) # 내컴퓨터에 돌아가고 있는 서버를 쓰겠다
db = client.dbsparta # dbsparta라는 이름의 db로 들어가겠다.(없으면 만들어짐_

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td.point

soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    img_tag = tr.select_one('img')
    star_tag = tr.select_one('td.point')

    a_tag = tr.select_one('td.title > div >a')
    if a_tag is not None:
        rank = img_tag.get('alt')
        # rank = img_tag['alt']
        star = star_tag.text
        title = a_tag.text

        doc = {
           'rank': rank,
           'title':title,
           'star':star
        }
        db.movies.insert_one(doc)
