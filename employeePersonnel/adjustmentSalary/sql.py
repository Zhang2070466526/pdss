def employee_adjustment_salary_sql(id_tuple,begin_date,end_date,adjustment_salary_type_tuple):  # 员工调薪历程
    sql= """
            SELECT
                pi.EmpID as ad_emp_id,
                po.PeriodName as ad_pd_name,
                pi.BasePay as ad_base_pay,
                pi.SalaryAdjustmentType as ad_salary_adjustment_type 
            FROM
                T_HR_PayItem AS pi 
                LEFT JOIN T_HR_Period AS po ON pi.MonthID= po.id 
            WHERE
                pi.EmpID in {}
            and po.BeginDate BETWEEN '{}' and '{}'
            and pi.SalaryAdjustmentType in {}
    """.format(id_tuple,begin_date,end_date,adjustment_salary_type_tuple)
    if adjustment_salary_type_tuple is None or len(adjustment_salary_type_tuple) == 0:
        sql = sql.replace("and pi.SalaryAdjustmentType in ()", "")
    return sql
