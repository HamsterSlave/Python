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