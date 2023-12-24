from haystack import indexes
from .models import HrEmployeeHistory

class HrEmployeeHistoryIndex(indexes.SearchIndex, indexes.Indexable):
    """
    文章索引数据模型类
    """
    text = indexes.CharField(document=True, use_template=True)
    # id = indexes.IntegerField(model_attr='id')
    employee_name = indexes.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')


    def get_model(self):
        """返回建立索引的模型类"""
        return HrEmployeeHistory

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.filter()



'''

python manage.py rebuild_index

'''
