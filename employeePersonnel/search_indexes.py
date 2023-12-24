# from django_elasticsearch_dsl import Document, Index, fields
# from django_elasticsearch_dsl.registries import registry
# # from .models import MyModel
# from .models import HrEmployeeHistory
# from elasticsearch_dsl import connections
# '''
#
# 你可以在 Django 的管理命令中使用这个模型来创建、查询、更新和删除数据库记录。
#
# 在创建 Elasticsearch 模型时，你需要指定一个 Django 模型，这个 Django 模型的数据将会被存储到 Elasticsearch 中。在这个示例中，HrEmployeeHistory 就是你需要指定的 Django 模型。
#
#
# '''
# @registry.register_document
# class MyModelDocument(Document):
#     class Index:  #class Index: 是一个内部类，它定义了 Elasticsearch 索引的名称和设置。在这个示例中，索引的名称是 my_HrEmployeeHistory，并且设置了索引的分片数量为 1，副本数量为 0。
#         name = 'my_HrEmployeeHistory'
#         settings = {'number_of_shards': 1, 'number_of_replicas': 0}
#
#     class Django:  #class Django: 是一个内部类，它定义了如何将 Django 模型的数据存储到 Elasticsearch 中。在这个示例中，它指定了模型是 HrEmployeeHistory，并且将 HrEmployeeHistory 模型的 employee_name 和 employee_code 字段存储到 Elasticsearch 中。
#         model = HrEmployeeHistory
#         fields = [
#             'employee_name',
#             'employee_code',
#         ]
#
# connections.create_connection()
# MyModelDocument.init()
# MyModelDocument.update_from_model(HrEmployeeHistory)
#
#
#
#
#
#
#
# '''
# python manage.py search_index --rebuild
# '''