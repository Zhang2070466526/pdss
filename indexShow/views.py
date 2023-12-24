from django.http import HttpResponse
from django.shortcuts import render
from indexShow.indexMethods.indexMethods import Index


# Create your views here.

def get_index_data(request):
    res = Index(request, "recruit_data")
    res = res.center_method()
    return res
