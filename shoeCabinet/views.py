from django.shortcuts import render
from .shoeFunction import Shoe
from .shoeFunction import Employee


# Create your views here.

def upload_info(request):
    shoe = Shoe(request=request)
    res = shoe.method_center("upload_info")
    return res


def get_list(request):
    shoe = Shoe(request=request)
    res = shoe.method_center("get_list")
    return res


def download_info(request):
    shoe = Shoe(request=request)
    res = shoe.method_center("download_info")
    return res


def edit_person(request):
    shoe = Shoe(request=request)
    res = shoe.method_center("edit_person")
    return res


def delete_person(request):
    shoe = Shoe(request=request)
    res = shoe.method_center("delete_person")
    return res


def create_single_info(request):
    shoe = Shoe(request=request)
    res = shoe.method_center("create_single_info")
    return res


# 新增报修信息
def add_repair(request):
    shoe = Employee(request=request)
    res = shoe.method_center("add_repair")
    return res


# 获取人员信息
def get_my_info(request):
    shoe = Employee(request=request)
    res = shoe.method_center("get_my_info")
    return res
