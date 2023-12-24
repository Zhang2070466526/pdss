# def transfer():
#     sql = """
#     select
#         EmpID as employee_id,                   -- 人员ID
#         TransferDate as mobilize_date,          -- 调职日期
#         case when OldDeptID == 0 then NONE else OldDeptID end as old_department_id,         -- 旧部门ID
#         OldPostID as old_position_id,           --原岗位ID
#         OldJobGradeID as old_job_grade_id,      --原职等ID
#         OldJobID as old_job_duty_id,            --原职务ID
#         OldJobClassID as old_job_class_id,      --原职类ID
#         OldPayTypeID as old_pay_type_id,        --旧计薪方式
#         OldJobRankID as old_job_rank_id,        --旧合同归属ID
#         OldJobSequenceID as old_job_sequence_id,--旧职级序列
#         OldCode as old_code,                    --旧工号
#         NewDeptID as new_department_id,         --新部门ID
#         NewPostID as new_position_id,           --新岗位ID
#         NewJobGradeID as new_job_grade_id,      --原职等ID
#         NewJobID as new_job_duty_id,            --新职务ID
#         NewJobClassID as new_job_class,         --新职类ID
#         NewPayTypeID as new_pay_type,           --新计薪方式
#         NewJobRankID as new_job_rank,           --新合同归属ID
#         NewJobSequenceID as new_job_sequence,   --新职级序列ID
#         NewCode as new_code,                    --新工号
#         TransferReason as mobilize_reason,      --调职原因
#         TransferType as mobilize_type,          --调职类型
#         BeforeDeptAdvice as mobilize_out_org_opinion, --调出组织意见
#         AfterDeptAdvice as mobilize_in_org_opinion,   --调入组织意见
#         HRAdvice as hr_opinion                --人事意见
#     FROM T_HR_Transfer
#     """
#     return sql
def transfer():
    sql = """
    SELECT
        EmpID AS employee_id, -- 人员ID
        TransferDate AS mobilize_date, -- 调职日期
        CASE WHEN OldDeptID = 0 THEN NULL ELSE OldDeptID END AS old_department_id, -- 旧部门ID
        CASE WHEN OldPostID = 0 THEN NULL ELSE OldPostID END AS old_position_id, -- 原岗位ID
        CASE WHEN OldJobGradeID = 0 THEN NULL ELSE OldJobGradeID END AS old_job_grade_id, -- 原职等ID
        CASE WHEN OldJobID = 0 THEN NULL ELSE OldJobID END AS old_job_duty_id, -- 旧部门ID
        CASE WHEN OldJobClassID = 0 THEN NULL ELSE OldJobClassID END AS old_job_class_id, -- 原职类ID
        CASE WHEN OldPayTypeID = 0 THEN NULL ELSE OldPayTypeID END AS old_pay_type_id, -- 旧计薪方式
        CASE WHEN OldJobRankID = 0 THEN NULL ELSE OldJobRankID END AS old_job_rank_id, -- 旧合同归属ID
        CASE WHEN OldJobSequenceID = 0 THEN NULL ELSE OldJobSequenceID END AS old_job_sequence_id, -- 旧职级序列
        OldCode AS old_code, -- 旧工号
        CASE WHEN NewDeptID = 0 THEN NULL ELSE NewDeptID END AS new_department_id, -- 新部门ID
        CASE WHEN NewPostID = 0 THEN NULL ELSE NewPostID END AS new_position_id, -- 新岗位ID
        CASE WHEN NewJobGradeID = 0 THEN NULL ELSE NewJobGradeID END AS new_job_grade_id, -- 新职等ID
        CASE WHEN NewJobID = 0 THEN NULL ELSE NewJobID END AS new_job_duty_id, -- 新职务ID
        CASE WHEN NewJobClassID = 0 THEN NULL ELSE NewJobClassID END AS new_job_class_id, -- 新职类ID
        CASE WHEN NewPayTypeID = 0 THEN NULL ELSE NewPayTypeID END AS new_pay_type_id, -- 新计薪方式
        CASE WHEN NewJobRankID = 0 THEN NULL ELSE NewJobRankID END AS new_job_rank_id, -- 新合同归属ID
        CASE WHEN NewJobSequenceID = 0 THEN NULL ELSE NewJobSequenceID END AS new_job_sequence_id, -- 新职级序列ID
        NewCode AS new_code, -- 新工号
        CASE WHEN OldDeptID = 0 THEN NULL ELSE OldDeptID END AS old_department_id, -- 旧部门ID
        TransferReason AS mobilize_reason, -- 调职原因
        TransferType AS mobilize_type, -- 调职类型
        BeforeDeptAdvice AS mobilize_out_org_opinion, -- 调出组织意见
        AfterDeptAdvice AS mobilize_in_org_opinion, -- 调入组织意见
        HRAdvice AS hr_opinion, -- 人事意见
        G_yrzrq AS old_join_date, -- 旧入职日期
        G_xrzrq AS new_join_date -- 新入职日期
    FROM
        T_HR_Transfer
    WHERE
        NewJobRankID != OldJobRankID
        
    """
    return sql
