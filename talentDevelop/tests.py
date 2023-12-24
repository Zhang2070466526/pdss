from django.test import TestCase

# Create your tests here.
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta

# def generate_dates(current_date):
#    dates = []
#    for month in range(1, 13):
#        if current_date <= date(2024, month, 31):
#            for i in range(3):
#                if month + i < 13:
#                   dates.append(date(2024, month + i, 31))
#                else:
#                   dates.append(date(2024, month + i - 12, 31))
#            break
#    return dates
#
# print(generate_dates(datetime(2024, 12, 2).date()))


a=dict({'currentPage': '1', 'pageSize': '25', 'month': '', 'baseNameId:': [9]})
print(a.get('baseNameId'))
