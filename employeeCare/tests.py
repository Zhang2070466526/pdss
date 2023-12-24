from django.test import TestCase

# Create your tests here.
a = ['employee_identity_file', 'employee_diploma_file']
b = ['employee_code', 'employee_name', 'employee_nationality', 'employee_identity_file', 'employee_diploma_file',
     'employee_department__department_name', 'employee_department__department_code', 'employee_identity_file__id',
     'employee_identity_file__employee_file_name', 'employee_identity_file__employee_file_url',
     'employee_identity_file__employee_file_status', 'employee_diploma_file__id',
     'employee_diploma_file__employee_file_name', 'employee_diploma_file__employee_file_url',
     'employee_diploma_file__employee_file_status']

result = list(set(b) - set(a))
print(result)
