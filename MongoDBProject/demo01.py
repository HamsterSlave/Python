import pymongo
from pymongo.database import Database

# 创建客户端-方式一
client = pymongo.MongoClient(host='127.0.0.1',port=27017,document_class=dict,tz_aware=False,connect=True,username='root',password='123456')
# print(client)
# # 创建客户端-方式二
# # url = "mongodb://root:123456@127.0.0.1:27017"
# url = "mongodb://%s:%s@%s:%s"%('root','123456','127.0.0.1','27017')
# client = pymongo.MongoClient(url)
# print(client)
# # 数据库-方式一
# db = client.runoob
# print(db)
# # 数据库-方式二
# db2 = Database(client=client,name='runoob')
# print(db2)
# # 数据库-方式三
# db3 = client.get_database('runoob')
# print(db3)
# # 删除数据库
# client.drop_database('runoob')
for db_name in client.list_database_names():
    print(db_name)

