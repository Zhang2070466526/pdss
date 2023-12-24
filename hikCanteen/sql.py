import arrow


# 每日新入职需充值饭卡人员
def daliy_entry_job_rank_person_sql(date):
    return """
                                        SELECT
                                            a.name,
                                            a.code,
                                            c.DepartmentName,
                                            d.PostName,
                                            e.JobLevelName,
                                            b.JobRankName,
                                            a._jtrzrq,
                                            b.entryCanteenAmount 
                                        FROM
                                            T_HR_Employee AS a
                                            left JOIN T_HR_JobRank AS b ON a.JobRankID = b.id
                                            left JOIN T_HR_Department AS c ON a.DeptID = c.id
                                            left JOIN T_HR_Post AS d ON a.PostID = d.id
                                            left JOIN T_HR_JobLevel AS e ON a.JobLevelID = e.id 
                                        WHERE
                                            a.EmployeeStatusID = 1 
                                            AND b.entryCanteenAmount IS NOT NULL 
                                            AND a.CreateTime >= '%s'
                                """ % date


# 不需要饭补人员，如昆山
def update_not_need_canteen_person_sql(code):
    return """
                                    UPDATE T_HR_Employee 
                                    SET if_canteen = 0 
                                    WHERE
                                        code = '%s'
                                    """ % code

# 已经首充人员
def update_need_canteen_person_sql(code):
    return """
                                    UPDATE T_HR_Employee 
                                    SET if_canteen = 1 
                                    WHERE
                                        code = '%s'
                                    """ % code

# 总部更新已有人脸人员至ehr
def update_zongbu_face_status(code):
    return """
                    UPDATE T_HR_Employee 
                    SET zongbu_photo = 1 
                    WHERE
                        code = '%s'
                    """ % code


# 建湖二期更新已有人脸人员至ehr
def update_jianhuerqi_face_status(code):
    return """
                    UPDATE T_HR_Employee 
                    SET jianhu_photo = 1 
                    WHERE
                        code = '%s'
                    """ % code


# 总部查找没有人脸用户
select_zongbu_no_face_employee = """
                    select code from T_HR_Employee 
                    WHERE
                        zongbu_photo is NULL  and EmployeeStatusID = 1
                    """

# 建湖二期更新已有人脸人员至ehr
select_jianhuerqi_no_face_employee = """
                    select code from T_HR_Employee 
                    WHERE
                        jianhu_photo is NULL  and EmployeeStatusID = 1
                    """

# 总部新入职人员
def select_zongbu_new_person(date):
    return """
                SELECT
                                    a.code,
                                    a.name,
                                    a.Sex,
                                    a.IdentityNumber,
                                    b.DepartmentCode
                                FROM
                                    T_HR_Employee AS a
                                    left JOIN T_HR_Department AS b ON a.DeptID = b.ID
                                WHERE
                                    a.zongbu_photo is NULL  and a.EmployeeStatusID = 1 and a.CreateTime > '%s'
                """%date
# 建湖二期新入职人员
def select_jianhuerqi_new_person(date):
    return """
                SELECT
                                    a.code,
                                    a.name,
                                    a.Sex,
                                    a.IdentityNumber,
                                    b.DepartmentCode
                                FROM
                                    T_HR_Employee AS a
                                    left JOIN T_HR_Department AS b ON a.DeptID = b.ID
                                WHERE
                                    a.jianhu_photo is NULL  and a.EmployeeStatusID = 1 and a.CreateTime > '%s'"""%date


def month_meal_allowance_sql(begin_time, end_time):
    return """
            SELECT
                b.code,
                b.name,
                b.EmployeeStatusID,
                c.name as 'banci',
                c.MstID,
                c.night,
                b.PayTypeID,
                d.id as 'job_rank_id',
                d.JobRankName,
                d.JobRankCode,
                e.JobLevelCode,
                e.JobLevelName,
                f.DepartmentCode,
                f.DepartmentName,
                g.PostName,
                a.WorkDate,
                a.b1sb,
                a.b1xb,
                a.sqjb,
                a.ycqxs,
                c.ifWork,
                ISNULL(a.BiaoZhun , 0) as 'BiaoZhun',
                a.JiaBan,
                ISNULL(a._ctxxs , 0) as '_ctxxs',
                ISNULL(a.cqxs, 0) as 'cqxs',
                ISNULL(a.ChuQin, 0) as 'ChuQin',
                ISNULL(a.OT1, 0) as 'OT1',
                ISNULL(a.OT2, 0) as 'OT2',
                ISNULL(a.OT3, 0) as 'OT3',
                ISNULL(a.OT4, 0) as 'OT4',
                ISNULL(a.njxs, 0) as 'njxs',
                ISNULL(a.sjxs, 0) as 'sjxs',
                ISNULL(a.bjxs, 0) as 'bjxs',
                ISNULL(a.hjxs, 0) as 'hjxs',
                ISNULL(a.njxs, 0) as 'njxs',
                ISNULL(a.cjxs, 0) as 'cjxs',
                ISNULL(a.gsxs, 0) as 'gsxs',
                ISNULL(a.txxs, 0) as 'txxs',
                ISNULL(a.sajxs, 0) as 'sajxs',
                ISNULL(a.pcjxs, 0) as 'pcjxs',
                ISNULL(a.cjjxs, 0) as 'cjjxs',
                ISNULL(a.hljxs, 0) as 'hljxs',
                ISNULL(a.brjxs, 0) as 'brjxs',
                ISNULL(a.ccxs, 0) as 'ccxs',
                ISNULL(a.yejxs, 0) as 'yejxs',
                ISNULL(a.wcxs, 0) as 'wcxs'
            FROM
                T_HR_WorkingTime AS a
                left JOIN T_HR_Employee AS b ON a.EmpID = b.id
                left JOIN T_HR_JobLevel as e on b.JobLevelID = e.id
                left JOIN T_HR_Department as f on b.DeptID = f.id
                left JOIN T_HR_ShiftsMst AS c ON a.ShiftID = c.MstID
                left JOIN T_HR_JobRank AS d ON d.id = b.JobRankID 
                left JOIN T_HR_Post as g on b.PostID = g.id
            WHERE
                d.entryCanteenAmount IS NOT NULL 
                --and d.id in (27, 45, 48, 49)
                and b.code = '2010009519'
                AND WorkDate BETWEEN '%s' 
                AND '%s'
            """%(begin_time, end_time)

