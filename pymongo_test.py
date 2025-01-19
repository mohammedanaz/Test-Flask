import pymongo

client = pymongo.MongoClient()
print(client.list_database_names())

db = client["school"]
students = db["students"]
students_data = students.find({},{"name":1, "_id":0, "place":1})
print(list(students_data))