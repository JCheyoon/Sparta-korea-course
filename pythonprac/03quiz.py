from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#매트릭스 영화의 별점을 출력
movie = db.movies.find_one({'title': '매트릭스'})
# print(movie['star'])

#매트릭스와 별점이 같은 영화 타이틀을 출력
mtch_star = movie['star']

same_star = list(db.movies.find({'star':match_star},{'_id':False}))

for target in same_star:
    print(target['title'])
