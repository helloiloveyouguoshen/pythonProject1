# from pymongo import MongoClient
# # class TestMongo:
# #     def __init__(self):
# client = MongoClient(host="127.0.0.1",port=27017)
# collection = client["admin"]["test"]
#     # def test_insert(self):
# collection.insert({"name":56,"age":33})
from pymongo import MongoClient

# 创建数据库连接对象
client = MongoClient()

# 选择一个数据库
db = client['admin']

# 身份认证
# db.authenticate('python', 'python')

# 选择一个集合
col = db['stu']

# 插入一条数据
col.insert({'a': 'b'})
