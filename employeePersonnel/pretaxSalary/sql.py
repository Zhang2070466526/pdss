def employee_payroll_sql(id_tuple,begin_date,end_date):  # 员工每月的薪资
    sql= """
        SELECT
                pr.EmpId as pr_emp_id,
                pi.PeriodName as pr_pi_name,
                pr._yfhj as pr_yfhj
        FROM
                T_HR_Payroll AS pr
                LEFT JOIN T_HR_Period AS pi ON pr.MonthID = pi.id 
        WHERE
            AppStatus=1 and
            pr.EmpId IN {}
            and pi.BeginDate BETWEEN '{}' and '{}'
    """.format(id_tuple,begin_date,end_date)
    return sql
