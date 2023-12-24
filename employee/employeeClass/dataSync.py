from utils.sqlServerConnect import OAConnect, EhrConnect
from employee.employeeClass.sync_sql import *
from employee.models import *
from django.db.models import Q
from datetime import datetime
from utils.save_data_to_redis import *
class DataSync:
    def __init__(self):
        self.oa = OAConnect()
        self.ehr = EhrConnect()
        self.now_time = ''

    def dept_Sync(self):
        result = self.ehr.select(dept_sync_sql(self.now_time))
        for i in result:
            # print(i)
            pk = i.pop('id')
            HrDepartment.objects.update_or_create(defaults=i, pk=pk)

        all_first_dept = list(HrDepartment.objects.filter( ~Q(id=999999),
            Q(department_expiry_date__isnull=True) | Q(
                department_expiry_date__gt=datetime.now()), department_status=1, department_level=2, ).values(
            'id','department_full_name', 'department_full_code'))  # 所有一级部门
        # print('all_first_dept',all_first_dept)

        all_center_dept = list(HrDepartment.objects.filter(Q(department_full_name__endswith='中心') | Q(department_full_name__endswith='研究院'),~Q(id=999999), Q(department_expiry_date__isnull=True) | Q(
            department_expiry_date__gt=datetime.now()), department_status=1, department_level=2,).values(
            'department_full_name','department_full_code','id'))  # 一级部门   中心
        # print(all_center_dept)
        all_business_dept= [first_dept for first_dept in all_first_dept if first_dept not in all_center_dept]    #一级部门 事业部
        # print(all_business_dept)
        all_business_dept_id=[business_dept['id'] for business_dept in all_business_dept]

        all_business_dept_children = list(HrDepartment.objects.filter(~Q(id=999999), Q(department_expiry_date__isnull=True) | Q(
            department_expiry_date__gt=datetime.now()), department_status=1, department_level=3,department_parent_id__in=all_business_dept_id).values(
            'department_full_name','department_full_code','id'))  # 事业部下面的所有二级部门
        # print(all_business_dept_children)
        save_list_data_to_redis('all_first_dept',all_first_dept)  # 所有一级部门
        save_list_data_to_redis('all_center_dept', all_center_dept)  # 一级部门的中心
        save_list_data_to_redis('all_business_dept', all_business_dept)  #  一级部门的事业部
        save_list_data_to_redis('all_business_dept_children', all_business_dept_children)  # 一级部门事业部下面的所有二级部门





    def position_Sync(self):
        result = self.ehr.select(position_sync_sql(self.now_time))
        for i in result:
            # print(i)
            pk = i.pop('id')
            HrPosition.objects.update_or_create(defaults=i, pk=pk)

    def jobClass_Sync(self):
        result = self.ehr.select(jobClass_sync_sql(self.now_time))
        for i in result:
            # print(i)
            pk = i.pop('id')
            HrJobClass.objects.update_or_create(defaults=i, pk=pk)

    def jobGrade_Sync(self):
        result = self.ehr.select(jobGrade_sync_sql(self.now_time))
        for i in result:
            # print(i)
            pk = i.pop('id')
            HrJobGrade.objects.update_or_create(defaults=i, pk=pk)

    def jobDuty_Sync(self):
        result = self.ehr.select(jobDuty_sync_sql(self.now_time))
        for i in result:
            # print(i)
            pk = i.pop('id')
            HrJobDuty.objects.update_or_create(defaults=i, pk=pk)

    def payType_Sync(self):
        result = self.ehr.select(payType_sync_sql(self.now_time))
        for i in result:
            # print(i)
            pk = i.pop('id')
            HrPayType.objects.update_or_create(defaults=i, pk=pk)

    def jobRank_Sync(self):
        result = self.ehr.select(jobRank_sync_sql(self.now_time))
        for i in result:
            # print(i)
            pk = i.pop('id')
            HrJobRank.objects.update_or_create(defaults=i, pk=pk)

    def Nation_Sync(self):
        result = self.ehr.select(Nation_sync_sql(self.now_time))
        for i in result:
            # print(i)
            pk = i.pop('id')
            HrNation.objects.update_or_create(defaults=i, pk=pk)

    def nationPlace_Sync(self):
        result = self.ehr.select(nationPlace_sync_sql(self.now_time))
        for i in result:
            # print(i)
            if i['nation_place_status'] is None:
                i['nation_place_status'] = True
            pk = i.pop('id')
            HrNationPlace.objects.update_or_create(defaults=i, pk=pk)

    def dimissionReason_sync(self):    #离职原因
        result = self.ehr.select(dimissionReason_sync_sql(self.now_time))
        for i in result:
            pk = i.pop('id')
            if i['dim_reason_type_id']==0 :
                i['dim_reason_type_id']=999999
            elif i['dim_reason_type_id'] is None:
                i['dim_reason_type_id'] = None
            HrDimissionReason.objects.update_or_create(defaults=i, pk=pk)


    # def dimissionReason_sync(self):    #离职原因
    #     result = self.ehr.select(dimissionReason_sync_sql(self.now_time))
    #     for i in result:
    #         pk = i.pop('id')
    #         # print(pk,i)
    #         HrDimissionReason.objects.update_or_create(defaults=i, pk=pk)


    def dimissionType_sync(self):    #离职类型
        result = self.ehr.select(dimissionType_sync_sql(self.now_time))
        for i in result:
            pk = i.pop('id')
            HrDimissionType.objects.update_or_create(defaults=i, pk=pk)

    def educationDegree_Sync(self):
        result = self.ehr.select(educationDegree_sync_sql(self.now_time))
        for i in result:
            # print(i)
            if i['edu_degree_status'] is None:
                i['edu_degree_status'] = True
            pk = i.pop('id')
            HrEducationDegree.objects.update_or_create(defaults=i, pk=pk)

    def employee_Sync(self):
        result = self.ehr.select(employee_sync_sql(self.now_time))
        for i in result:
            pk = i.pop('id')
            HrEmployee.objects.update_or_create(defaults=i, pk=pk)
