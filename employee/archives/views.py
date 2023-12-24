from rest_framework.views import APIView


from employee.archives.privateMethods.archivesAll import *
from employee.archives.privateMethods.archivesByPerson import *
from employee.archives.privateMethods.archivesByType import *



class Categorized_By_Type_RecordView(APIView):
    def post(self, request, **kwargs):
        new_query = ArchivesByType(request, 'categorized_by_type')
        query = new_query.method_center()
        return query

    pass
class Categorized_By_Person_RecordView(APIView):
    def post(self, request, **kwargs):
        new_query = ArchivesByPerson(request, 'categorized_by_person')
        query = new_query.method_center()
        return query

class All_Ingredients_RecordView(APIView):   #全部材料
    def post(self, request, **kwargs):
        new_query = ArchivesAll(request, 'all_ingredients')
        query = new_query.method_center()
        return query