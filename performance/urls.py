from django.urls import path,include,re_path


urlpatterns = [

    path('eRoadInterface/',include('performance.eRoadInterface.urls')),    # eRoadInterface

]