def daliy_attendance_data_sql(employee_code, begin_date, end_date):
    return """
                SELECT
                    CONVERT(varchar(100), a.WorkDate, 23) as 'work_date',
	                case when a._yczt1 is null then '正常' else a._yczt1 end as 'attendance_status'
                FROM
                    T_HR_WorkingTime AS a
                    INNER JOIN T_HR_Employee AS b ON a.EmpID = b.id 
                WHERE
                    b.code = '%s' 
                    AND a.WorkDate BETWEEN '%s' 
                    AND '%s'
                    """ % (employee_code, begin_date, end_date)


def someday_attendance_data_sql(employee_code, date):
    return """
        SELECT
            a.b1sb,
            a.b1xb,
            a.b2sb,
            a.b2xb
        FROM
            T_HR_WorkingTime AS a
            INNER JOIN T_HR_Employee AS b ON a.EmpID = b.id 
        WHERE
            b.code = '%s' 
            AND a.WorkDate = '%s'
    """ % (employee_code, date)
