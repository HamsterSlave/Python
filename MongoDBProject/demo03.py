import pymongo
from pymongo.collection import Collection


# 创建客户端
uri = "mongodb://%s:%s@%s:%s" % ('root', '123456', '127.0.0.1', '27017')
client = pymongo.MongoClient(uri)
# 获取数据库
db = client.runoob
users = db.pxcoder

def show(rs):
    for r in rs:
        print(r)

def query_and():
    r = users.find({'age':24,'gender':'男'})
    show(r)

def query_or():
    r = users.find({'$or':[{'age':24},{'gender':'男'}]})
    show(r)

def query_and_or():
    r = users.find({'gender':'男','$or':[{'age':24},{'favorite':'有娃人生'}]})
    show(r)

if __name__ == '__main__':
    query_and_or()