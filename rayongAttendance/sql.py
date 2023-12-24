import arrow


def select_Rayong_Attendance_sql(startData, endData):
    if startData != '':
        startData = startData + " 00:00:00"
    if endData != '':
        endData = endData + " 23:59:59"
    return """
        SELECT pin, event_time, reader_name
        FROM acc_transaction
        WHERE (reader_name LIKE '%罗勇三期大门出1-1-出%' OR reader_name LIKE '%罗勇三期大门出2-1-出%') AND 
        event_time BETWEEN '{0}' AND '{1}' AND pin != ''
        group by pin,event_time,reader_name
        order by event_time ASC
        
    """ .format(startData, endData)


def select_ehr_workNumber_sql(code, startTime, endTime):
    return """
       SELECT 
            emp.Code,
            emp.Name,
            dp.DepartmentCode,
            dp.DepartmentName,
            sm.Name as 'job_time',
                 CONVERT(datetime, CONVERT(date, wt.WorkDate, 112)) + CONVERT(datetime, CONVERT(time, sm.beginTime)) AS startTime,
                    DATEADD(DAY, CASE WHEN sm.night = 1 THEN 1 ELSE 0 END, 
                 DATEADD(DAY, DATEDIFF(DAY, 0, CONVERT(DATE, wt.WorkDate)), CONVERT(DATETIME, sm.endTime)))
            AS endTime

       FROM 
           T_HR_Employee AS emp
           INNER JOIN T_HR_WorkingTime AS wt ON emp.id = wt.EmpID
           INNER JOIN T_HR_ShiftsMst AS sm ON wt.ShiftID = sm.MstID
           INNER JOIN T_HR_Department as dp on emp.DeptID = dp.id
    WHERE
        emp.Code = '%s' AND sm.beginTime IS NOT NULL AND sm.endTime IS NOT NULL AND wt.WorkDate BETWEEN '%s' AND '%s' """ % (code,startTime,endTime)