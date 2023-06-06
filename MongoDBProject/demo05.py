import pymongo
from pymongo.collection import Collection


# 创建客户端
uri = "mongodb://%s:%s@%s:%s" % ('root', '123456', '127.0.0.1', '27017')
client = pymongo.MongoClient(uri)
# 获取数据库
db = client.runoob
users = db.users

def show(rs):
    for r in rs:
        print(r)

def query_multi():
    r = users.find({'USERID':{'$regex':'^R049'}})
    print("*******")
    show(r)
    r1 = users.find({'USERID': {'$regex': '451$'}})
    print("*******")
    show(r1)
    r2 = users.find({'USERID': {'$regex': '451$'}},{'USERID':1})
    print("*******")
    show(r2)

if __name__ == '__main__':
    query_multi()