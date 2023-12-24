def get_month_salary_sql(code, period):
    return """
            SELECT
                c.PeriodName,
                b.Name,
                d.DepartmentName,
                e.PostName,
                a.BasePay,--基本工资
                a.PostSalary,--岗位工资
                a._jxgz,--绩效工资
                a._hfbt,--话费补贴
                a._yfjbgz,--应发基本工资
                a._yfgwgz,--应发岗位工资
                a._jxzhxs,--绩效综合系数
                a._yfjxgz,--绩效
                a._jjbt,--奖金/津贴
                a._yfbthj,--补贴合计
                a._yfhj,--应发合计
                a._ljljhj,--社保公积金个人承担
                a._gryangl as grylao,--个人养老
                a._gryil as gryliao,--个人医疗
                a._grdb as grdb,--个人大病
                a._grsy as grsy, --个人失业
                a._gjjgr as grgjj,--个人公积金
                a._grhj+a._gjjgr as grhj,
                a._dwhj+ a._gjjdw as 'sbgjjdw',--社保公积金单位承担
                a._dkgs,--代扣个税
                a._shuidf,--水费/电费
                a._fangzf,--房租费/物业费
                a.RealPay,--实发工资
                a.remark --薪资备注
                
            FROM
                T_HR_Payroll AS a
                INNER JOIN T_HR_Employee AS b ON a.EmpID = b.id
                INNER JOIN T_HR_Period AS c ON a.MonthID = c.ID
                INNER JOIN T_HR_Department AS d ON b.DeptID = d.id
                INNER JOIN T_HR_Post AS e ON b.PostID = e.ID 
            WHERE
                b.code = '%s' 
                AND c.PeriodName = '%s';
                """ % (code, period)


def get_year_salary_list_sql(code, year):
    return """
                SELECT
                c.id,
                c.PeriodName,
                case when a.wxStatus is NULL then 3 else a.wxStatus end as wxStatus
            FROM
                T_HR_Payroll AS a
                INNER JOIN T_HR_Employee AS b ON a.EmpID = b.id
                INNER JOIN T_HR_Period AS c ON a.MonthID = c.ID 
            WHERE
                b.code = '%s' and a.AppStatus = '1'
                AND c.PeriodName LIKE '%%%s%%'
                ORDER BY c.PeriodName;
    """ % (code, year)
