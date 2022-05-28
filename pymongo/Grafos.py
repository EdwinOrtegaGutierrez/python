import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["world"]
mycol = mydb["areas"]
mylist = [
{ "_id" : 1, "name" : "Asia" },
{ "_id" : 2, "name" : "China", "belongsto" : "Asia" },
{ "_id" : 3, "name" : "ZheJiang", "belongsto" : "China" },
{ "_id" : 4, "name" : "HangZhou", "belongsto" : "ZheJiang" },
{ "_id" : 5, "name" : "NingBo", "belongsto" : "ZheJiang" },
{ "_id" : 6, "name" : "Xihu", "belongsto" : "HangZhou" }
]
x = mycol.insert_many(mylist)
for x in mycol.find():
  print(x)
