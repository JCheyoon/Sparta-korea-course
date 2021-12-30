import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number

for tr in trs:
    a_rank = tr.select_one('td.number')
    a_tag = tr.select_one('td.info > a.title.ellipsis')
    a_artist = tr.select_one('td.info > a.artist.ellipsis')
    if a_tag is not None:
        rank = a_rank.text[0:2].strip() #text[0:2]
        title = a_tag.text.strip() #strip is removing emtpy spaces , begining and end of string
        artist = a_artist.text.strip()
        print(rank,title,artist)
