# 部门同步
def dept_sync_sql(now_time):
    return """
        SELECT  
        ID as id,
        DepartmentCode as department_code ,
        DepartmentName as department_name ,
        FullCode as department_full_code ,
        FullName as department_full_name ,
        shortname as department_short_name ,
        D_glgs as department_manage,
        DeptLeve as department_level,
        ParentID as department_parent_id,
        Dept1 as department_first_name,
        Dept2 as department_second_name,
        Dept3 as department_third_name,
        Dept4 as department_forth_name,
        IfUse as department_status,
        ExpiryDate as department_expiry_date
        FROM T_HR_Department  where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)


def position_sync_sql(now_time):
    return """
    select 
    ID as id,
    PostCode as position_code,
    PostName as position_name,
    IfUse as department_status
    from T_HR_Post where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)


def jobClass_sync_sql(now_time):
    return """
    select 
    ID as id,
    JobClassCode as job_class_code,
    JobClassName as job_class_name,
    IfUse as job_class_status
    FROM T_HR_JobClass where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)


def jobGrade_sync_sql(now_time):
    return """
    select 
    ID as id,
    JobGradeName as job_grade_name,
    JobGradeCode as job_grade_code,
    IfUse as job_grade_status
    from T_HR_JobGrade where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)



def jobDuty_sync_sql(now_time):
    return """
    select 
    ID as id,
    JobCode as job_duty_code,
    JobName as job_duty_name,
    JobClassID as job_duty_class_id,
    JobGradeID as job_duty_grade_id,
    IfUse as job_duty_status
    from T_HR_Job where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)



def payType_sync_sql(now_time):
    return """
    select 
    ID as id,
    PayTypeCode as pay_type_code,
    PayTypeName as pay_type_name,
    IfUse as pay_type_status
    from T_HR_PayType where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)



def jobRank_sync_sql(now_time):
    return """
    select 
    ID as id,
    JobRankCode as job_rank_code,
    JobRankName as job_rank_name,
    Remark as job_rank_remark,
    IfUse as job_rank_status
    from T_HR_JobRank where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)



def Nation_sync_sql(now_time):
    return """
    select 
    ID as id,
    NationCode as nation_code,
    NationName as nation_name,
    IfUse as nation_status
    from T_HR_Nation where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)



def nationPlace_sync_sql(now_time):
    return """
    select 
    ID as id,
    NativeCode as nation_place_code,
    NativeName as nation_place_name,
    IfUse as nation_place_status
    from T_HR_Native where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)

def dimissionReason_sync_sql(now_time):#离职原因
    return """
    select 
    ID as id,
    DimissionReasonCode as dim_reason_code,
    DimissionReasonName as dim_reason_name,
    DimissionTypeID as dim_reason_type_id,
    IfUse as dim_reason_status
    from T_HR_DimissionReason 
    --where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)

# def dimissionReason_sync_sql(now_time):#离职原因
#     return """
#     select
#     ID as id,
#     DimissionReasonCode as dim_reason_code,
#     DimissionReasonName as dim_reason_name,
#     IfUse as edu_degree_status
#     from T_HR_DimissionReason where CreateTime >= '%s' or ModifyTime >= '%s'
#     """ % (now_time, now_time)


def dimissionType_sync_sql(now_time):#离职类型
    return """
    select 
    ID as id,
    TypeCode as dim_type_code,
    TypeName as dim_type_name,
    IfUse as dim_type_status
    from T_HR_DimissionType where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)

def educationDegree_sync_sql(now_time):
    return """
    select 
    ID as id,
    DegreeCode as edu_degree_code,
    DegreeName as edu_degree_name,
    IfUse as edu_degree_status
    from T_HR_Degree where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)



def employee_sync_sql(now_time):
    return """
    select 
    ID as id,
    Name as employee_name,
    Code as employee_code,
    _gzd as employee_work_place,
    phone as employee_phone,
    _gj as employee_nationality,
    email as employee_email,
    case when DeptID = 0 then NULL else DeptID end as employee_department_id,
    case when PostID = 0 then NULL else PostID end as employee_position_id,
    EmployeeStatusID as employee_status,
    _dlidl as employee_dl,
    Sex as employee_sex,
    IdentityType as employee_identity_type,
    IdentityNumber as employee_identity_no,
    case when JobID = 0 then NULL else JobID end as employee_job_duty_id,
    case when JobClassID = 0 then NULL else JobClassID end as employee_job_class_id,
    case when JobGradeID = 0 then NULL else JobGradeID end as employee_job_grade_id,
    case when PayTypeID = 0 then NULL else PayTypeID end as employee_pay_type_id,
    case when JobRankID = 0 then NULL else JobRankID end as employee_job_rank_id,
    case when JobSequenceID = 0 then NULL else JobSequenceID end as  employee_job_sequence_id,
    HireDate as employee_join_date,
    _jtrzrq as employee_group_join_date,
    DimissionDate as employee_departure_date,
    _lztbrq as employee_departure_notice_date,
    _lzblrq as employee_departure_handle_date,
    PlanTurnDate as employee_plan_turn_date,
    TurnDate as employee_turn_date,
    TurnStatus as employee_turn_status,
    case when NationID = 0 then NULL else NationID end as employee_nation_id,
    case when HomeID = 0 then NULL else HomeID end as employee_nation_place_id,
    marriage as employee_marriage_status,
    case when DegreeID = 0 then NULL else DegreeID end as employee_first_degree_id,
    IssuingDate as employee_identity_no_effective_date,
    DueDate as employee_identity_no_failre_date,
    Birthday as employee_birthday,
    HomeAddress as employee_nation_address,
    _ygzt as employee_work_status,
    _zzmm as employee_political_status,
    --_rygzjl as employee_work_experience,
    EmergencyContact as employee_emergency_contact,
    EmergencyCall as employee_emergency_contact_phone,
    ContactRelationship as employee_emergency_contact_relation,
    _yuanxiao as employee_first_degree_school,
    _zhuanye as employee_first_degree_major,
    --_bysj as employee_first_degree_graduate_date,
    _jyfs as employee_first_degree_type,
    _zuigxl as employee_train_degree,
    G_jxxx as employee_train_degree_school,
    G_jxzy as employee_train_degree_major,
    --G_jxbysj as employee_train_degree_graduate_date,
    G_jxfs as employee_train_degree_type,
    _kahao as employee_bank_no,
    _khh as employee_bank_deposit,
    _gwmc as employee_process,
    case when DimissionReasonID = 0 then NULL else DimissionReasonID end as employee_dim_reason_id,
    case when DimissionTypeID=0 then Null else DimissionTypeID end as employee_dim_type_id,    --离职类型
    
    qq as employee_labor_source
    from T_HR_Employee where CreateTime >= '%s' or ModifyTime >= '%s'
    """ % (now_time, now_time)

