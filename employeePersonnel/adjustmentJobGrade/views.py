from utils.genericMethods import ViewBasicTemplate
from .methods import BasicMobilize, MobilizeInfoFileClass
from datetime import datetime, timedelta
import openpyxl,os
from pdss.settings import BASE_DIR
from django.http import JsonResponse
import pandas as pd
class basicDepartInfo(ViewBasicTemplate):
    def __init__(self):
        super().__init__(BasicMobilize)


class fileMobilizeInfo(ViewBasicTemplate):
    def __init__(self):
        super().__init__(MobilizeInfoFileClass)

