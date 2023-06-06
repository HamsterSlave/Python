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

# 年龄小于30
def query_lt():
    r = users.find({'age':{'$lt':30}})
    show(r)

# 年龄大于31
def query_gt():
    r = users.find({'age':{'$gt':31}})
    show(r)
# 年龄为18/24/26的文档
def query_in():
    r = users.find({'age':{'$in':[18,24,26]}})
    show(r)
# 有favorite域的文档
def query_exists():
    r = users.find({'favorite':{'$exists':True}})
    show(r)

if __name__ == '__main__':
    query_exists()
