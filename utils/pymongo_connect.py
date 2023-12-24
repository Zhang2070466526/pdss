from pymongo import MongoClient

class MongoDBHelper:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client.get_database("mydatabase")    #数据库名

    def find_documents(self, collection_name, query={}):
        collection = self.db[collection_name]
        return collection.find(query)

    def update_document(self, collection_name, filter_query, update_query):
        collection = self.db[collection_name]
        return collection.update_one(filter_query, update_query)

    def delete_document(self, collection_name, filter_query):
        collection = self.db[collection_name]
        return collection.delete_one(filter_query)

    def close_connection(self):
        self.client.close()

# # 示例用法
# if __name__ == "__main__":
#     connection_string = "mongodb://localhost:27017/"
#     database_name = "mydatabase"
#     helper = MongoDBHelper(connection_string, database_name)
#
#     # 查询文档
#     query = {"name": "John"}
#     documents = helper.find_documents("mycollection", query)
#     for document in documents:
#         print(document)
#
#     # 更新文档
#     filter_query = {"name": "John"}
#     update_query = {"$set": {"age": 31}}
#     result = helper.update_document("mycollection", filter_query, update_query)
#     print(f"Updated {result.modified_count} document(s)")
#
#     # 删除文档
#     filter_query = {"name": "John"}
#     result = helper.delete_document("mycollection", filter_query)
#     print(f"Deleted {result.deleted_count} document(s)")
#
#     helper.close_connection()
