from pymongo import MongoClient #파이몽고를 쓰겠다
client = MongoClient('localhost', 27017) # 내컴퓨터에 돌아가고 있는 서버를 쓰겠다
db = client.dbsparta # dbsparta라는 이름의 db로 들어가겠다.(없으면 만들어짐_

# insert / find / update / delete

#insert :
# doc = {'name':'Jane','age':21}
# db.users.insert_one(doc) # db안에 users라는 콜렌션 안에 doc하나를 넣어라

# #find
# user = db.users.find_one({'name':'Peti'})
# print(user)
# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

#Update
# db.users.update_one({'name':'Jessie'},{'$set':{'age':28}})
# db.users.update_many({'name':'Jessie'},{'$set':{'age':28}}) 모든 jessie를 찾아 age를28로 바꿔라

#delete
db.users.delete_one({'name':'bobby'})
db.users.delete_many({'name':'bobby'})
