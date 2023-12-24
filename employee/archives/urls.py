from django.urls import path,include,re_path
from . import views
# from Anomalies.urls import views




urlpatterns = [

    path('categorized_by_person/',views.Categorized_By_Person_RecordView.as_view()),   #  按人员分类
    path('Categorized_by_type/',views.Categorized_By_Type_RecordView.as_view()),       #  按类型分类
    path('all_ingredients/',views.All_Ingredients_RecordView.as_view()),       #  全部材料
]