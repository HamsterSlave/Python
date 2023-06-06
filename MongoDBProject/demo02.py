import pymongo
from pymongo.collection import Collection


# 创建客户端
url = "mongodb://%s:%s@%s:%s" % ('root', '123456', '127.0.0.1', '27017')
client = pymongo.MongoClient(url)
# 获取数据库
db = client.runoob

def test_collection():
    # 获取集合-方式一
    runoob = db.runoob
    print(runoob)
    # 获取集合-方式二
    runoob2 = Collection(db, 'runoob')
    print(runoob2)
    # 获取集合-方式三
    runoob3 = db.get_collection('runoob')
    print(runoob3)
    # # 获取集合-方式四
    # runoob4 = db.create_collection('col')
    # print(runoob4)
    # for db_name in client.list_database_names():
    #     print(db_name)

    # 删除集合
    db.drop_collection("col")
    # show collections
    for cols in db.list_collections():
        print(cols)

def test_index():
    users = client.runoob.pxcoder
    idx = users.create_index([('name',pymongo.DESCENDING)])
    print(idx)
    # idx2 = users.create_index([('age',pymongo.DESCENDING)])
    # print(idx2)
    # #联合索引
    # idx3 = users.create_index([('name',pymongo.DESCENDING),('status',pymongo.ASCENDING)])
    # print(idx3)
    # #唯一索引
    # idx4 = users.create_index([('name',pymongo.ASCENDING)],unique=True)
    # print(idx4)
    #删除索引
    # users.drop_index('name_1')
    # users.drop_indexs()

def test_insert():
    users = client.runoob.pxcoder
    r = users.insert_one({'name':'鲍伟新','age':26})
    print(r)
    print(r.acknowledged,r.inserted_id)
    #插入多条文档
    rs = users.insert_many([{'name':'韩邦胜','age':26,'gender':'男'},{'name':'白传松','age':24,'gender':'男'},{'name':'王运好','age':24,'gender':'男'}],ordered=True)

def test_delete():
    users = client.runoob.pxcoder
    # r = users.delete_one({'name':'鲍伟新'})
    # if r.acknowledged:
    #     print("删除%s条数据成功！" % (r.deleted_count))
    rs = users.delete_many({'name':'王运好'})
    if rs.acknowledged:
        print("删除%s条数据成功！" % (rs.deleted_count))

def test_update():
    users = client.runoob.pxcoder
    # #更新一条
    # r = users.update_one(filter={'name':'鲍伟新'},update={'$set':{'name':'王焱','gender':'男','favorite':'品鉴数码产品'}})
    # if r.acknowledged:
    #     print("更新成功！")
    #更新多条
    rs =  users.update_many(filter={'name':'焦方进'},update={'$set':{'age':32}})
    if  rs.acknowledged:
        print("更新成功！")


if __name__ == '__main__':
    # test_index()
    # test_insert()
    # test_delete()
    test_update()