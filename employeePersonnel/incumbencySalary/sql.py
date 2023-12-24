def employee_newest_transfer_sql(id_tuple):  # 员工最新的调职查询
    return """
        SELECT 
            ts1.EmpID as ts_emp_id,
            ts1.TransferDate as ts_date,
            ts1.TransferType as  ts_type,
            ts1.CreateTime as ts_create_time
        FROM T_HR_Transfer as ts1
        JOIN (
         SELECT EmpID, max(CreateTime) as max_date
         FROM T_HR_Transfer
         GROUP BY EmpID
        ) ts2 ON ts1.EmpID = ts2.EmpID AND ts1.CreateTime = ts2.max_date
        where  ts1.EmpID in {}
    """.format(id_tuple)


def employee_newest_payitem_sql(id_tuple):  # 员工最新的调薪查询
    return """
        SELECT
            pi.SalaryDate as pi_salary_date ,
            pi.SalaryAdjustmentType as pi_salary_adjustment_type,
            pi.EmpID as pi_emp_id
        FROM
            T_HR_PayItem AS pi 
        WHERE
            pi.CreateTime = ( SELECT MAX ( CreateTime ) FROM T_HR_PayItem AS pi2 WHERE pi2.EmpId = pi.EmpId ) 
            AND pi.EmpId IN {}
    """.format(id_tuple)


def employee_asskpi_sql(id_tuple,begin_date,end_date,jx_grade_tuple):  # 员工每月的绩效
    sql= """
        SELECT
            ak.EmpId as ak_emp_id,
            po.PeriodName as ak_pd_name,
            ak._grdf as ak_grdf,
            --ak.AppStatus as akkk
            ak._grjg as ak_grjg
        FROM
            T_Mis_AssKPI AS ak
            LEFT JOIN T_Mis_AssPeriod AS po ON ak.PeriodID= po.id 
        WHERE
            ak.EmpId IN {}
            and po.BeginDate BETWEEN '{}' and '{}'
            and ak._grjg  in {}
    """.format(id_tuple,begin_date,end_date,jx_grade_tuple)
    if jx_grade_tuple is None or len(jx_grade_tuple) == 0:
        sql = sql.replace("and ak._grjg  in ()", "")
    return sql

