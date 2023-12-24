from django.urls import path

from . import views

urlpatterns = [
    path('login', views.admin_login, name='admin_login'),
    path('logout', views.admin_logout, name='admin_logout'),
    path('sidebar', views.admin_sidebar, name='admin_sidebar'),   #旧的
    path('editpwd',views.admin_editpwd, name='admin_editpwd'),
    path('picbk',views.admin_picbk, name='admin_editpwd'),
    path('getnav', views.admin_getnav, name='admin_getnav'),
    path('getsidebar', views.admin_getsidebar, name='getsidebar')   #新的

]
