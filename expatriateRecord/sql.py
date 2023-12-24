import json
import os

import arrow
import openpyxl
from rest_framework.status import *
from auther.models import AdminUser
from utils.sqlServerConnect import EhrConnect,OAConnect
from utils.abstract import ExpatriateOptions


class ExpatriateQuality(ExpatriateOptions):
    def select(self):
        sql = """
            SELECT
                expatriate_type_name  as 'value',
                expatriate_type_name  as 'label'
            FROM
                T_HR_ExpatriateType 
            WHERE
                status = 1
                AND expatriate_type_name <> ''
                
        """
        ehr_connect = EhrConnect()
        return ehr_connect.select(sql)

    def options(self):
        sql = """
            SELECT
                expatriate_type_name as 'value',
                expatriate_type_name  as 'label'
            FROM
                T_HR_ExpatriateType 
            WHERE
                status = 1
                AND expatriate_type_name <> ''
        """
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        temp = {}
        for data in data_list:
            temp[data['label']] = data['value']
        return temp

class ExpatriateType:
    def select(self):
        sql = """
            SELECT DISTINCT
              COALESCE(a.fd_3b69529de2396c, '') AS 'value',
              COALESCE(a.fd_3b69529de2396c, '') AS 'label'
            FROM 
              ekp_18971c10f086762f16a4 AS a
            WHERE
               a.fd_3b69529de2396c <> ''
        """
        oa_connect = OAConnect()
        data_list = oa_connect.select(sql)
        return data_list

class ExpatriatePlace(ExpatriateOptions):
    def select(self):
        sql = """
            SELECT
                expatriate_place_name as 'value',
                expatriate_place_name  as 'label'
            FROM
                T_HR_ExpatriatePlace 
            WHERE
                status = 1
                AND expatriate_place_name <> ''
        """
        ehr_connect = EhrConnect()
        return ehr_connect.select(sql)

    def options(self):
        sql = """
              SELECT
                expatriate_place_name as 'value',
                expatriate_place_name  as 'label'
            FROM
                T_HR_ExpatriatePlace 
            WHERE
                status = 1
                AND expatriate_place_name <> ''
        """
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        temp = {}
        for data in data_list:
            temp[data['label']] = data['value']
        return temp


class ExpatriateReEnterVisa(ExpatriateOptions):
    def select(self):
        sql = """
            SELECT
                re_enter_visa_name as 'value',
                re_enter_visa_name  as 'label'
            FROM
                T_HR_ExpatriateReEnterVisa 
            WHERE
                status = 1
                AND re_enter_visa_name <> ''
        """
        ehr_connect = EhrConnect()
        return ehr_connect.select(sql)

    def options(self):
        sql = """
            SELECT
                re_enter_visa_name as 'value',
                re_enter_visa_name  as 'label'
            FROM
                T_HR_ExpatriateReEnterVisa 
            WHERE
                status = 1
                AND re_enter_visa_name <> ''
        """
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        temp = {}
        for data in data_list:
            temp[data['label']] = data['value']
        return temp


class ExpatriateVisaType(ExpatriateOptions):
    def select(self):
        sql = """
            SELECT
                visa_type_name as 'value',
                visa_type_name  as 'label'
            FROM
                T_HR_ExpatriateVisaType 
            WHERE
                status = 1
                AND visa_type_name <> ''
        """

        ehr_connect = EhrConnect()
        return ehr_connect.select(sql)

    def options(self):
        sql = """
            SELECT
                visa_type_name as 'value',
                visa_type_name  as 'label'
            FROM
                T_HR_ExpatriateVisaType 
            WHERE
                status = 1
                AND visa_type_name <> ''
        """
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        temp = {}
        for data in data_list:
            temp[data['label']] = data['value']
        return temp


class ExpatriateVisaHandleStatus(ExpatriateOptions):
    def select(self):
        sql = """
            SELECT
                visa_handle_status_name as 'value',
                visa_handle_status_name  as 'label'
            FROM
                T_HR_ExpatriateVisaHandleStatus 
            WHERE
                status = 1
                AND visa_handle_status_name <> ''
        """
        ehr_connect = EhrConnect()
        return ehr_connect.select(sql)

    def options(self):
        sql = """
             SELECT
                visa_handle_status_name as 'value',
                visa_handle_status_name  as 'label'
            FROM
                T_HR_ExpatriateVisaHandleStatus 
            WHERE
                status = 1
                AND visa_handle_status_name <> ''
        """
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        temp = {}
        for data in data_list:
            temp[data['label']] = data['value']
        return temp


class ExpatriateRank(ExpatriateOptions):  #职级
    def select(self):
        sql = """
            SELECT
                JobGradeName as 'value',
                JobGradeName  as 'label'
            FROM
                T_HR_JobGrade
            WHERE
                ifUse = 1
        """
        ehr_connect = EhrConnect()
        return ehr_connect.select(sql)

    def options(self):
        sql = """
             SELECT
                JobGradeName as 'value',
                JobGradeName  as 'label'
            FROM
                T_HR_JobGrade
            WHERE
                ifUse = 1
        """
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        temp = {}
        for data in data_list:
            temp[data['label']] = data['value']
        return temp

class ExpatriateJobclass(ExpatriateOptions):#职等
    def select(self):
        sql = """
             SELECT
                 JobClassName as 'value',
                 JobClassName  as 'label'
             FROM
                 T_HR_JobClass
             WHERE
                 ifUse = 1
         """
        ehr_connect = EhrConnect()
        return ehr_connect.select(sql)

    def options(self):
        sql = """
              SELECT
                 JobClassName as 'value',
                 JobClassName  as 'label'
             FROM
                 T_HR_JobClass
             WHERE
                 ifUse = 1
         """
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        temp = {}
        for data in data_list:
            temp[data['label']] = data['value']
        return temp


class ExpatriateDept:
    def select(self,code):
        sql = """
            SELECT DISTINCT
                FullName as 'value',
                FullName  as 'label'
            FROM
                T_HR_Department
            WHERE
                IfUse = 1 AND
                FullName LIKE '%{}%'
        """.format(code)
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        return data_list

class AbbreviationDept:#部门简称
    def select(self,code):
        sql = """
            SELECT DISTINCT
                shortname as 'value',
                shortname  as 'label'
            FROM
                T_HR_Department
            WHERE
                IfUse = 1 AND
                shortname LIKE '%{}%'
                AND shortname <> ''
        """.format(code)
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        return data_list

class ExpatriateManage:
    def select(self, code):
        sql = """
            SELECT DISTINCT
                D_glgs as 'value',
                D_glgs  as 'label'
            FROM
                T_HR_Department
            WHERE
                IfUse = 1 AND
                D_glgs LIKE '%{}%'
        """.format(code)
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        return data_list

class ExpatriatePost:
    def select(self, code):
        sql = """
            SELECT DISTINCT
                PostName as 'value',
                PostName  as 'label'
            FROM
                T_HR_Post
            WHERE
                IfUse = 1 AND
                PostName LIKE '%{}%'
        """.format(code)
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        return data_list

class ExpatriateJobrank:
    def select(self):
        sql = """
            SELECT DISTINCT
                JobRankName as 'value',
                JobRankName  as 'label'
            FROM
                T_HR_JobRank
            WHERE
                IfUse = 1
        """
        ehr_connect = EhrConnect()
        data_list = ehr_connect.select(sql)
        return data_list



class Employee:
    def select(self, code):
        ehr_connect = EhrConnect()
        # sql = """
        # SELECT
        #     id AS 'label',
        #     code + '--' + name AS 'value'
        #
        # FROM
        #     T_HR_Employee
        # WHERE
        #     name LIKE '%%%s%%'
        # """ % (code)

        sql ="""
            SELECT
                b.code,
                b.name,
                b.IdentityNumber as idCard,
                b._jtrzrq as date_Of_Entry,
                d.D_glgs AS expatriate_Before_Manage,
                c.JobRankName AS expatriate_jobRank,
                d.shortname AS abbreviation_Dept,
                e.PostName AS post,
                d.FullName AS expatriate_Dept,
                f.JobGradeName AS rank,
                g.JobClassName AS expatriate_jobClass
            FROM
                T_HR_Employee AS b 
                LEFT JOIN T_HR_Employee_File AS fi ON fi.employee_id= b.id
                LEFT JOIN T_HR_JobRank AS c ON b.JobRankID = c.id
                LEFT JOIN T_HR_Department AS d ON b.DeptID = d.id
                LEFT JOIN T_HR_Post AS e ON b.PostID = e.id 
                left JOIN T_HR_JobGrade AS f ON b.JobGradeID = f.id
                LEFT JOIN T_HR_JobClass as g on b.JobClassID =g.id
            WHERE
                 d.IfUse= 1 
                AND c.IfUse= 1 
                AND e.IfUse= 1
                AND f.IfUse=1
                AND b.DimissionTypeID is null
                AND b.code LIKE '%%%s%%'""" % (code)
        select_back = ehr_connect.select(sql)

        if select_back:
            return {'msg': '查询成功',
                    'data': select_back,
                    'code': 200,
                    }, HTTP_200_OK
        else:
            return {'msg': '',
                    'data': [],
                    }, HTTP_200_OK

    @staticmethod
    def select_rank_idCard_abbreviation_Dept():
        sql = """
            SELECT
                b.code AS code,
                f.JobGradeName AS rank,
                b.IdentityNumber AS idCard,
                d.shortname AS abbreviation_Dept 
            FROM
                T_HR_Employee AS b
                LEFT JOIN T_HR_JobGrade AS f ON b.JobGradeID = f.id
                LEFT JOIN T_HR_Department AS d ON b.DeptID = d.id 
            WHERE
                d.IfUse= 1 
                AND d.IfUse= 1 --AND b.DimissionTypeID is null
                AND f.IfUse= 1
        """
        ehr_connect = EhrConnect()
        return ehr_connect.select(sql)




class ExpatriateRecordOA:
    @staticmethod
    def select():
        oa_connect = OAConnect()
        total_Data = oa_connect.select("""
                SELECT
                    a.fd_3b6954604e4f38 AS code,
                    d.fd_name AS name,
                    a.fd_3b6950f8d4d0ae AS date_Of_Entry,
                    a.fd_3b6954712518e8 AS expatriate_Dept,
                    a.fd_3b6950ff04c378 AS post,
                    a.fd_3bce086965932c_text AS expatriate_jobRank,
                    a.fd_3b859b63c6f666_text AS expatriate_Before_Base,
                    a.fd_3b696bd6f00e76_text AS expatriate_Before_Manage,
                    a.fd_3b696c09c53d9a_text AS expatriate_Before_Factory,
                    b.fd_name AS resident_Dept,

                    --a.fd_3b697d7c70a53e AS waipaizhouqinian,
                    --a.fd_3b697d8288a3ae AS waipaizhouqiyue,
                    CONCAT(
                            CASE WHEN a.fd_3b697d7c70a53e <> 0 AND a.fd_3b697d7c70a53e IS NOT NULL THEN CONCAT(a.fd_3b697d7c70a53e, '年') ELSE '' END,
                            CASE WHEN a.fd_3b697d8288a3ae <> 0 AND a.fd_3b697d8288a3ae IS NOT NULL THEN CONCAT(a.fd_3b697d8288a3ae, '月') ELSE '' END
                    ) AS expatriate_Cycle,
                    a.fd_3b69519342d04c AS expatriate_Begin,
                    a.fd_3b69519c604f82 AS expatriate_End,
                    --a.fd_3b696c7c1884d4 AS isCross_Division,
                    CASE
                        WHEN a.fd_3b696c7c1884d4 = '是' THEN 1
                        WHEN a.fd_3b696c7c1884d4 = '否' THEN 0
                        ELSE NULL
                    END AS isCross_Division,
                    a.fd_3b859baba3e302_text AS expatriate_After_Base,
                    a.fd_3b83f888444d4e_text AS expatriate_After_Manage,
                    a.fd_3b83f898a0d922_text AS expatriate_After_Factory,
                    a.fd_3b84015c746fc4 AS expatriate_Reason,
                    a.fd_3b84015e11640e AS expatriate_Target,
                    a.fd_3b69527750dcea AS expatriate_Allowance,
                    a.fd_3b84027639e682 AS description_Allowance,
                    a.fd_3b69529de2396c AS expatriate_Type,
                    a.fd_3b696d74a1810c AS expatriate_After_Cost,
                    c.doc_status,
                    c.fd_ended_time,   --流程结束时间
                    c.fd_create_time
           
                FROM
                    ekp_18971c10f086762f16a4 AS a
                    INNER JOIN sys_org_element AS b ON a.fd_3b697405cafa40 = b.fd_id
                    INNER JOIN sys_org_element AS d ON a.fd_3b696a3e4d1584 = d.fd_id
                    INNER JOIN lbpm_process AS c ON a.fd_id = c.fd_id
                where c.doc_status = 30
                ORDER BY c.fd_create_time DESC;
        """)

        if total_Data:
            return {'msg': '查询成功',
                    'data': total_Data,
                    'code': 200,
                    }, HTTP_200_OK
        else:
            return {'msg': '',
                    'data': [],
                    }, HTTP_200_OK


    @staticmethod
    def selectIncrement():
        oa_connect = OAConnect()
        total_Data = oa_connect.select("""
                   SELECT
                       a.fd_3b6954604e4f38 AS code,
                       d.fd_name AS name,
                        CASE
                                WHEN a.fd_3b6950f8d4d0ae IS NOT NULL THEN a.fd_3b6950f8d4d0ae
                                ELSE a.fd_ruZhiRiQi
                        END AS date_Of_Entry,
                       a.fd_3b6954712518e8 AS expatriate_Dept,
                       a.fd_3b6950ff04c378 AS post,
                       -- a.fd_heTongGuiShu AS expatriate_jobRank,
                        CASE
                                WHEN a.fd_3bce086965932c_text IS NOT NULL THEN a.fd_3bce086965932c_text
                                ELSE a.fd_heTongGuiShu
                        END AS expatriate_jobRank,
                       a.fd_3b859b63c6f666_text AS expatriate_Before_Base,
                       -- a.fd_3b696bd6f00e76_text AS expatriate_Before_Manage,
                       a.fd_3b696c09c53d9a_text AS expatriate_Before_Factory,
                       b.fd_name AS resident_Dept,

                       --a.fd_3b697d7c70a53e AS waipaizhouqinian,
                       --a.fd_3b697d8288a3ae AS waipaizhouqiyue,
                       CONCAT(
                               CASE WHEN a.fd_3b697d7c70a53e <> 0 AND a.fd_3b697d7c70a53e IS NOT NULL THEN CONCAT(a.fd_3b697d7c70a53e, '年') ELSE '' END,
                               CASE WHEN a.fd_3b697d8288a3ae <> 0 AND a.fd_3b697d8288a3ae IS NOT NULL THEN CONCAT(a.fd_3b697d8288a3ae, '月') ELSE '' END
                       ) AS expatriate_Cycle,
                       a.fd_3b69519342d04c AS expatriate_Begin,
                       a.fd_3b69519c604f82 AS expatriate_End,
                       --a.fd_3b696c7c1884d4 AS isCross_Division,
                       CASE
                           WHEN a.fd_3b696c7c1884d4 = '是' THEN 1
                           WHEN a.fd_3b696c7c1884d4 = '否' THEN 0
                           ELSE NULL
                       END AS isCross_Division,
                       a.fd_3b859baba3e302_text AS expatriate_After_Base,
                       a.fd_3b83f888444d4e_text AS expatriate_After_Manage,
                       a.fd_3b83f898a0d922_text AS expatriate_After_Factory,
                       a.fd_3b84015c746fc4 AS expatriate_Reason,
                       a.fd_3b84015e11640e AS expatriate_Target,
                       a.fd_3b69527750dcea AS expatriate_Allowance,
                       a.fd_3b84027639e682 AS description_Allowance,
                       a.fd_3b69529de2396c AS expatriate_Type,
                       a.fd_3b696d74a1810c AS expatriate_After_Cost,
                       
                       a.fd_jinTieBiZhong AS expatriate_allowance_currency,
                       a.fd_qiTa AS expatriate_other,
                       a.fd_shengHuoBuTie AS expatriate_life,
                       a.fd_jianKuBuTie AS expatriate_hardship,
                       -- a.fd_zhiDeng AS expatriate_jobClass,
                       CASE
                                WHEN a.fd_paiZhuRenYuanZhiDeng IS NOT NULL THEN a.fd_paiZhuRenYuanZhiDeng
                                ELSE a.fd_zhiDeng
                        END AS expatriate_jobClass,
                       
                       
                       a.fd_waiPaiGuoJia  AS expatriate_country,
                       a.fd_diJiCiWaiPai AS expatriate_several_frequency,
                       -- a.fd_guanLiGuiShu AS expatriate_Before_Manage,
                        CASE
                                WHEN a.fd_3b696bd6f00e76_text IS NOT NULL THEN a.fd_3b696bd6f00e76_text
                                ELSE a.fd_guanLiGuiShu
                        END AS expatriate_Before_Manage,
                       
                       c.doc_status,
                       c.fd_ended_time,   --流程结束时间
                       c.fd_create_time

                   FROM
                       ekp_18971c10f086762f16a4 AS a
                       INNER JOIN sys_org_element AS b ON a.fd_3b697405cafa40 = b.fd_id
                       INNER JOIN sys_org_element AS d ON a.fd_3b696a3e4d1584 = d.fd_id
                       INNER JOIN lbpm_process AS c ON a.fd_id = c.fd_id
                   where c.doc_status = 30
                         AND c.fd_ended_time BETWEEN DATEADD(hour,-2, GETDATE()) AND GETDATE()   --前2小时的数据
                   ORDER BY c.fd_create_time ASC;
           """)

        if total_Data:
            return {'msg': '查询成功',
                    'data': total_Data,
                    'code': 200,
                    }, HTTP_200_OK
        else:
            return {'msg': '',
                    'data': [],
                    }, HTTP_200_OK


    @staticmethod
    def select_count():  #计算外派次数 和首次外派时间  上次外派起止时间
        sql="""
            SELECT 
                code,
                COUNT(*) AS number_Of_Expatriate,
                MIN(min_begin) AS first_Expatriate
            --     MIN(min_end) AS min_end,
            --     MAX(max_begin) AS max_begin,
            --     MAX(max_end) AS max_end,
             --   CASE WHEN COUNT(*) =1 or COUNT(*) =2  THEN MIN(min_begin) ELSE MAX(CASE WHEN fd_3b69519342d04c < max_begin THEN fd_3b69519342d04c END) END AS last_Expatriate_Begin,
             --   CASE WHEN COUNT(*) =1 or COUNT(*) =2 THEN MIN(min_end) ELSE MAX(CASE WHEN fd_3b69519c604f82 < max_end THEN fd_3b69519c604f82 END) END AS last_Expatriate_End
            FROM (
                SELECT 
                    a.fd_3b6954604e4f38 AS code,
                    a.fd_3b69519342d04c,
                    a.fd_3b69519c604f82,
                    MIN(a.fd_3b69519342d04c) OVER (PARTITION BY a.fd_3b6954604e4f38) AS min_begin,
                    MIN(a.fd_3b69519c604f82) OVER (PARTITION BY a.fd_3b6954604e4f38) AS min_end,
                    MAX(a.fd_3b69519342d04c) OVER (PARTITION BY a.fd_3b6954604e4f38) AS max_begin,
                    MAX(a.fd_3b69519c604f82) OVER (PARTITION BY a.fd_3b6954604e4f38) AS max_end
                FROM 
                    ekp_18971c10f086762f16a4 AS a
                INNER JOIN 
                    sys_org_element AS b ON a.fd_3b697405cafa40 = b.fd_id
                INNER JOIN 
                    sys_org_element AS d ON a.fd_3b696a3e4d1584 = d.fd_id
                INNER JOIN 
                    lbpm_process AS c ON a.fd_id = c.fd_id
                WHERE 
                    c.doc_status = 30
            ) AS subquery
            GROUP BY  code;
        """
        oa_connect = OAConnect()
        select_back = oa_connect.select(sql)
        if select_back:
            return {'msg': '查询成功',
                    'data': select_back,
                    'code': 200,
                    }, HTTP_200_OK
        else:
            return {'msg': '',
                    'data': [],
                    }, HTTP_200_OK


#上次外派开始时间:找出
