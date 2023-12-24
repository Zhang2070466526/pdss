# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 14:47
# @Author  : zhuang
# @Site    : 
# @File    : sql.py
# @Software: PyCharm
def select_person(startTime, endTime):
    return """
        SELECT
            a.fd_gongHao,
            a.fd_shenQingRenXingMing,
            a.fd_gaiYuanGongShiFuXuQiYongJin,
            a.fd_qiShiRi,
            a.fd_jieShuRi,
            a.fd_shenQingBuMen

        FROM
            ekp_lizhisq AS a
            INNER JOIN lbpm_process AS b ON a.fd_id = b.fd_id 
        WHERE
            b.doc_status = 30 
            and a.fd_gaiYuanGongShiFuXuQiYongJin = '是'
            AND b.fd_ended_time BETWEEN '{0}' 
            AND '{1}'
        """.format(startTime, endTime)


def select_person_info(code):
    return """
        SELECT A.Code, A.Name, A.IdentityNumber, B.JobRankName
        FROM T_HR_Employee AS A
        LEFT JOIN T_HR_JobRank as B ON A.JobRankID=B.ID
        WHERE A.Code='{0}'
    """.format(code)
