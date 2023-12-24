import json

from django.http import HttpResponse

from recruit.models import RecruitSal, RecruitIdl, RecruitDl
from salarySurvey.models import SalarySurveyRecord
from memorabilia.models import MemorabiliaList
from externalHonors.models import ExternalHonorsList
from internalEvaluation.models import InternalEvaluationList
from employeeActivities.models import EmployeeActivitiesList
from rewardsPunishments.models import RewardsAndPunishments, ProjectBonus
from employeeCare.models import ExitInterviews, Colloquium, JobInterviews, TalentSubsidies
from employeeInspect.models import EmployeeInspect
from auther.models import *

import arrow
from django.db.models import Sum, Count


class Index:
    def __init__(self, request, method):
        self.request = request
        self.user_base = ''
        self.token = ''
        self.return_data = {}
        self.now = ''
        self.last_month = ''
        self.method = method
        self.meth = {
            "recruit_data": self.recruit_data,
        }

    def center_method(self):
        self.user_base = self.request.user_base
        self.token = self.request.check_token
        self.now = arrow.now().format("YYYY-MM")
        self.last_month = arrow.now().shift(months=-1).format("YYYY-MM")
        if self.token == '':
            pass
        self.meth[self.method]()
        return HttpResponse(json.dumps(self.return_data))

    def dl(self):
        data_dl_month = RecruitDl.objects.filter(recruit_dl_status=1, recruit_dl_base_id__in=self.user_base,
                                                 recruit_dl_date__year=self.now[0:4],
                                                 recruit_dl_date__month=self.last_month[5:7]) \
            .values("recruit_dl_entry_no", "recruit_dl_to_entry_no", "recruit_dl_demand_no") \
            .aggregate(recruit_dl_entry_no=Sum('recruit_dl_entry_no'),
                       recruit_dl_to_entry_no=Sum("recruit_dl_to_entry_no"),
                       recruit_dl_demand_no=Sum("recruit_dl_demand_no"))
        data_dl_year = RecruitDl.objects.filter(recruit_dl_status=1, recruit_dl_base_id__in=self.user_base,
                                                recruit_dl_date__year=self.now[0:4], ) \
            .values("recruit_dl_entry_no", "recruit_dl_to_entry_no", "recruit_dl_demand_no") \
            .aggregate(recruit_dl_entry_no=Sum('recruit_dl_entry_no'),
                       recruit_dl_to_entry_no=Sum("recruit_dl_to_entry_no"),
                       recruit_dl_demand_no=Sum("recruit_dl_demand_no"))
        data_dl_year = self.judge_number(data_dl_year)
        data_dl_month = self.judge_number(data_dl_month)
        if data_dl_year['recruit_dl_demand_no'] == 0:
            data_dl_year['recruit_dl_completion_rate'] = 0
        else:
            data_dl_year['recruit_dl_completion_rate'] = round(
                (data_dl_year['recruit_dl_entry_no'] + data_dl_year['recruit_dl_to_entry_no']) / data_dl_year[
                    'recruit_dl_demand_no'], 2)
        if data_dl_month['recruit_dl_demand_no'] == 0:
            data_dl_month['recruit_dl_completion_rate'] = 0
        else:
            data_dl_month['recruit_dl_completion_rate'] = round(
                (data_dl_month['recruit_dl_entry_no'] + data_dl_month['recruit_dl_to_entry_no']) / data_dl_month[
                    'recruit_dl_demand_no'], 2)
        data = [
            {
                'label': 'DL月完成率(上个月)',
                'value': str(int(data_dl_month['recruit_dl_completion_rate'] * 100)) + '%'
            }, {
                'label': 'DL年完成率(今年)',
                'value': str(int(data_dl_year['recruit_dl_completion_rate'] * 100)) + '%',
            },
        ]
        if 'recruit' not in self.return_data['data']['big_card']:
            self.return_data['data']['big_card']['recruit'] = {
                'title': "招聘",
                'tip': "",
                'btns': []
            }
        self.return_data['data']['big_card']['recruit']['btns'].append(data[0])
        self.return_data['data']['big_card']['recruit']['btns'].append(data[1])

    def idl(self):
        data_idl_month = RecruitIdl.objects.filter(recruit_idl_status=1, recruit_idl_base_id__in=self.user_base,
                                                   recruit_idl_date__year=self.now[0:4],
                                                   recruit_idl_date__month=self.last_month[5:7]) \
            .values("recruit_idl_entry_no", "recruit_idl_to_entry_no", "recruit_idl_demand_no") \
            .aggregate(recruit_idl_entry_no=Sum('recruit_idl_entry_no'),
                       recruit_idl_to_entry_no=Sum("recruit_idl_to_entry_no"),
                       recruit_idl_demand_no=Sum("recruit_idl_demand_no"))
        data_idl_year = RecruitIdl.objects.filter(recruit_idl_status=1, recruit_idl_base_id__in=self.user_base,
                                                  recruit_idl_date__year=self.now[0:4]) \
            .values("recruit_idl_entry_no", "recruit_idl_to_entry_no", "recruit_idl_demand_no") \
            .aggregate(recruit_idl_entry_no=Sum('recruit_idl_entry_no'),
                       recruit_idl_to_entry_no=Sum("recruit_idl_to_entry_no"),
                       recruit_idl_demand_no=Sum("recruit_idl_demand_no"))
        data_idl_month = self.judge_number(data_idl_month)
        data_idl_year = self.judge_number(data_idl_year)
        if data_idl_year['recruit_idl_demand_no'] == 0:
            data_idl_year['recruit_idl_completion_rate'] = 0
        else:
            data_idl_year['recruit_idl_completion_rate'] = round(
                (data_idl_year['recruit_idl_entry_no'] + data_idl_year['recruit_idl_to_entry_no']) / data_idl_year[
                    'recruit_idl_demand_no'], 2)
        if data_idl_month['recruit_idl_demand_no'] == 0:
            data_idl_month['recruit_idl_completion_rate'] = 0
        else:
            data_idl_month['recruit_idl_completion_rate'] = round(
                (data_idl_month['recruit_idl_entry_no'] + data_idl_month['recruit_idl_to_entry_no']) / data_idl_month[
                    'recruit_idl_demand_no'], 2)
        data = [
            {
                'label': 'IDL月完成率(上个月)',
                'value': str(int(data_idl_month['recruit_idl_completion_rate'] * 100)) + '%'
            }, {
                'label': 'IDL年完成率(今年)',
                'value': str(int(data_idl_year['recruit_idl_completion_rate'] * 100)) + '%',
            },
        ]
        if 'recruit' not in self.return_data['data']['big_card']:
            self.return_data['data']['big_card']['recruit'] = {
                'title': "招聘",
                'tip': "",
                'btns': []
            }
        self.return_data['data']['big_card']['recruit']['btns'].append(data[0])
        self.return_data['data']['big_card']['recruit']['btns'].append(data[1])

    def sal(self):
        data_sal_month = RecruitSal.objects.filter(recruit_sal_status=1,
                                                   recruit_sal_base_id__in=self.user_base,
                                                   recruit_sal_date__year=self.now[0:4],
                                                   recruit_sal_date__month=self.last_month[5:7]) \
            .values("recruit_sal_entry_no", "recruit_sal_to_entry_no", "recruit_sal_demand_no") \
            .aggregate(recruit_sal_entry_no=Sum('recruit_sal_entry_no'),
                       recruit_sal_to_entry_no=Sum("recruit_sal_to_entry_no"),
                       recruit_sal_demand_no=Sum("recruit_sal_demand_no"))
        data_sal_year = RecruitSal.objects.filter(recruit_sal_status=1, recruit_sal_base_id__in=self.user_base,
                                                  recruit_sal_date__year=self.now[0:4], ) \
            .values("recruit_sal_entry_no", "recruit_sal_to_entry_no", "recruit_sal_demand_no") \
            .aggregate(recruit_sal_entry_no=Sum('recruit_sal_entry_no'),
                       recruit_sal_to_entry_no=Sum("recruit_sal_to_entry_no"),
                       recruit_sal_demand_no=Sum("recruit_sal_demand_no"))
        data_sal_month = self.judge_number(data_sal_month)
        data_sal_year = self.judge_number(data_sal_year)
        if data_sal_month['recruit_sal_demand_no'] == 0:
            data_sal_month['recruit_sal_completion_rate'] = 0
        else:
            data_sal_month['recruit_sal_completion_rate'] = round(
                (data_sal_month['recruit_sal_entry_no'] + data_sal_month['recruit_sal_to_entry_no']) / data_sal_month[
                    'recruit_sal_demand_no'], 2)
        if data_sal_year['recruit_sal_demand_no'] == 0:
            data_sal_year['recruit_sal_completion_rate'] = 0
        else:
            data_sal_year['recruit_sal_completion_rate'] = round(
                (data_sal_year['recruit_sal_entry_no'] + data_sal_year['recruit_sal_to_entry_no']) / data_sal_year[
                    'recruit_sal_demand_no'], 2)
        data = [
            {
                'label': 'SAL月完成率(上个月)',
                'value': str(int(data_sal_month['recruit_sal_completion_rate'] * 100)) + '%'
            }, {
                'label': 'SAL年完成率(今年)',
                'value': str(int(data_sal_year['recruit_sal_completion_rate'] * 100)) + '%',
            },
        ]
        if 'recruit' not in self.return_data['data']['big_card']:
            self.return_data['data']['big_card']['recruit'] = {
                'title': "招聘",
                'tip': "",
                'btns': []
            }
        self.return_data['data']['big_card']['recruit']['btns'].append(data[0])
        self.return_data['data']['big_card']['recruit']['btns'].append(data[1])

    def salarySurvey(self):
        salarySurveyData_month = SalarySurveyRecord.objects.filter(
            status=1,
            salary_base_id__in=self.user_base,
            period__year=self.now[0:4],
            period__month=self.now[5:7]).values("id").count()
        salarySurveyData_year = SalarySurveyRecord.objects.filter(
            status=1,
            salary_base_id__in=self.user_base,
            period__year=self.now[0:4], ).values("id").count()
        salarySurveyData_month = self.judge_number(salarySurveyData_month)
        salarySurveyData_year = self.judge_number(salarySurveyData_year)
        data = {
            'title': "薪资调研人数(本月)",
            "value": salarySurveyData_month,
            'subTitle': "人数(年)",
            'subValue': salarySurveyData_year,
            'unitColor': 'success',
            'unit': '月'
        }
        self.return_data['data']['small_card'].append(data)

    def MemorabiliaList(self):
        MemorabiliaListData_year = MemorabiliaList.objects.filter(
            memorabilia_status=1,
            memorabilia_base_id__in=self.user_base,
            memorabilia_date__year=self.now[0:4]).values("id").count()
        MemorabiliaListData_month = MemorabiliaList.objects.filter(
            memorabilia_status=1,
            memorabilia_base_id__in=self.user_base,
            memorabilia_date__year=self.now[0:4],
            memorabilia_date__month=self.now[5:7]).values("id").count()
        MemorabiliaListData_year = self.judge_number(MemorabiliaListData_year)
        MemorabiliaListData_month = self.judge_number(MemorabiliaListData_month)
        data = {
            'title': "大事记数量(本月)",
            "value": MemorabiliaListData_month,
            'subTitle': "数量(年)",
            'subValue': MemorabiliaListData_year,
            'unitColor': 'success',
            'unit': '月'
        }
        self.return_data['data']['small_card'].append(data)

    def externalHonorsList(self):
        externalHonorsListData_year = ExternalHonorsList.objects.filter(
            honor_status=1,
            honor_base_id__in=self.user_base,
            honor_date__year=self.now[0:4], ).values("id").count()
        externalHonorsListData_month = ExternalHonorsList.objects.filter(
            honor_status=1,
            honor_base_id__in=self.user_base,
            honor_date__year=self.now[0:4],
            honor_date__month=self.now[5:7]).values("id").count()
        externalHonorsListData_month = self.judge_number(externalHonorsListData_month)
        externalHonorsListData_year = self.judge_number(externalHonorsListData_year)
        data = {
            'title': "外部荣誉数量(本月)",
            "value": externalHonorsListData_month,
            'subTitle': "数量(年)",
            'subValue': externalHonorsListData_year,
            'unitColor': 'success',
            'unit': '月'
        }
        self.return_data['data']['small_card'].append(data)

    def InternalEvaluationList(self):
        InternalEvaluationListData_year = InternalEvaluationList.objects.filter(
            awards_status=1,
            evaluation_company_id__in=self.user_base,
            awards_date__year=self.now[0:4]).values("id").count()
        InternalEvaluationListData_month = InternalEvaluationList.objects.filter(
            awards_status=1,
            evaluation_company_id__in=self.user_base,
            awards_date__year=self.now[0:4],
            awards_date__month=self.now[5:7]).values("id").count()
        InternalEvaluationListData_year = self.judge_number(InternalEvaluationListData_year)
        InternalEvaluationListData_month = self.judge_number(InternalEvaluationListData_month)
        data = {
            'title': "内部评优数量(本月)",
            "value": InternalEvaluationListData_month,
            'subTitle': "数量(年)",
            'subValue': InternalEvaluationListData_year,
            'unitColor': 'success',
            'unit': '月'
        }
        self.return_data['data']['small_card'].append(data)

    def employeeActivitiesList(self):
        employeeActivitiesListData_year = EmployeeActivitiesList.objects.filter(
            employee_activities_status=1,
            employee_base_id__in=self.user_base,
            employee_activities_date__year=self.now[0:4]).values("id").count()
        employeeActivitiesListData_month = EmployeeActivitiesList.objects.filter(
            employee_activities_status=1,
            employee_base_id__in=self.user_base,
            employee_activities_date__year=self.now[0:4],
            employee_activities_date__month=self.now[5:7]).values("id").count()
        employeeActivitiesListData_year = self.judge_number(employeeActivitiesListData_year)
        employeeActivitiesListData_month = self.judge_number(employeeActivitiesListData_month)
        data = [
            {
                'label': '员工活动数量(本月)',
                'value': employeeActivitiesListData_month
            }, {
                'label': '数量(年)',
                'value': employeeActivitiesListData_year,
            }
        ]
        self.return_data['data']['big_card']['employeeActivitiesList'] = {
            'title': "员工活动",
            'tip': "",
            'btns': data
        }

    # 项目奖金
    def ProjectBonus(self):
        ProjectBonusData_month = ProjectBonus.objects.filter(
            project_bonus_status=1,
            project_bonus_base_id__in=self.user_base,
            project_bonus_date__year=self.now[0:4],
            project_bonus_date__month=self.now[5:7]).values("project_bonus_reach_no", 'project_bonus_total').aggregate(
            project_bonus_reach_no=Sum('project_bonus_reach_no'), project_bonus_total=Sum('project_bonus_total'))
        ProjectBonusData_year = ProjectBonus.objects.filter(
            project_bonus_status=1,
            project_bonus_base_id__in=self.user_base,
            project_bonus_date__year=self.now[0:4], ).values("project_bonus_reach_no", 'project_bonus_total').aggregate(
            project_bonus_reach_no=Sum('project_bonus_reach_no'), project_bonus_total=Sum('project_bonus_total'))

        ProjectBonusData_month = self.judge_number(ProjectBonusData_month)
        ProjectBonusData_year = self.judge_number(ProjectBonusData_year)
        data = [
            {
                'label': '奖励人数(本月)',
                'value': ProjectBonusData_month['project_bonus_reach_no']
            }, {
                'label': '奖励金额(本月)',
                'value': ProjectBonusData_month['project_bonus_total'],
            }, {
                'label': '奖励人数(年)',
                'value': ProjectBonusData_year['project_bonus_reach_no']
            }, {
                'label': '奖励金额(年)',
                'value': ProjectBonusData_year['project_bonus_total'],
            },
        ]
        self.return_data['data']['big_card']['ProjectBonus'] = {
            'title': "项目奖金",
            'tip': "",
            'btns': data
        }

    # 奖惩
    def RewardsAndPunishments(self):
        RewardsAndPunishmentsData_year = RewardsAndPunishments.objects.filter(
            r_p_status=1,
            r_p_base_id__in=self.user_base,
            r_p_date__year=self.now[0:4], ).values("rewards_person_no", 'rewards_money', 'punishments_person_no',
                                                   'punishments_money').aggregate(
            rewards_person_no=Sum('rewards_person_no'), rewards_money=Sum('rewards_money'),
            punishments_person_no=Sum('punishments_person_no'), punishments_money=Sum('punishments_money'),
        )
        RewardsAndPunishmentsData_month = RewardsAndPunishments.objects.filter(
            r_p_status=1,
            r_p_base_id__in=self.user_base,
            r_p_date__year=self.now[0:4],
            r_p_date__month=self.now[5:7]
        ).values("rewards_person_no", 'rewards_money', 'punishments_person_no', 'punishments_money').aggregate(
            rewards_person_no=Sum('rewards_person_no'), rewards_money=Sum('rewards_money'),
            punishments_person_no=Sum('punishments_person_no'), punishments_money=Sum('punishments_money'),
        )
        RewardsAndPunishmentsData_month = self.judge_number(RewardsAndPunishmentsData_month)
        RewardsAndPunishmentsData_year = self.judge_number(RewardsAndPunishmentsData_year)
        data = [
            {
                'label': '奖励人数(本月)',
                'value': RewardsAndPunishmentsData_month['rewards_person_no']
            }, {
                'label': '奖励金额(本月)',
                'value': RewardsAndPunishmentsData_month['rewards_money'],
            }, {
                'label': '奖励人数(年)',
                'value': RewardsAndPunishmentsData_year['rewards_person_no']
            }, {
                'label': '奖励金额(年)',
                'value': RewardsAndPunishmentsData_year['rewards_money'],
            },
        ]
        self.return_data['data']['big_card']['Rewards'] = {
            'title': "奖惩-奖",
            'tip': "",
            'btns': data
        }
        data = [
            {
                'label': '奖励人数(本月)',
                'value': RewardsAndPunishmentsData_month['punishments_person_no']
            }, {
                'label': '奖励金额(本月)',
                'value': RewardsAndPunishmentsData_month['punishments_money'],
            }, {
                'label': '奖励人数(年)',
                'value': RewardsAndPunishmentsData_year['punishments_person_no']
            }, {
                'label': '奖励金额(年)',
                'value': RewardsAndPunishmentsData_year['punishments_money'],
            },
        ]
        self.return_data['data']['big_card']['Punishments'] = {
            'title': "奖惩-惩",
            'tip': "",
            'btns': data
        }

    # 在职访谈
    def JobInterviews(self):
        JobInterviewsData_year = JobInterviews.objects.filter(job_interviews_base_id__in=self.user_base,
                                                              job_interviews_status=1,
                                                              job_interviews_date__year=self.now[0:4]).values(
            "job_interviews_number").aggregate(job_interviews_number=Sum('job_interviews_number'))
        JobInterviewsData_month = JobInterviews.objects.filter(job_interviews_base_id__in=self.user_base,
                                                               job_interviews_status=1,
                                                               job_interviews_date__year=self.now[0:4],
                                                               job_interviews_date__month=self.last_month[5:7]
                                                               ).values("job_interviews_number",
                                                                        "job_interviews_percentage",
                                                                        "job_interviews_outputItem",
                                                                        "job_interviews_closeItem") \
            .aggregate(job_interviews_number=Sum("job_interviews_number"),
                       job_interviews_closeItem=Sum("job_interviews_closeItem"),
                       job_interviews_outputItem=Sum("job_interviews_outputItem"))
        JobInterviewsData_month = self.judge_number(JobInterviewsData_month)
        JobInterviewsData_year = self.judge_number(JobInterviewsData_year)
        if JobInterviewsData_month['job_interviews_outputItem'] == 0:
            JobInterviewsData_month['job_interviews_completionRate'] = '0%'
        else:
            JobInterviewsData_month['job_interviews_completionRate'] = str(int(round(
                JobInterviewsData_month['job_interviews_closeItem'] / JobInterviewsData_month[
                    'job_interviews_outputItem'], 2) * 100)) + '%'
        data = [
            {
                'label': '访谈人数(上个月)',
                'value': JobInterviewsData_month['job_interviews_number']
            }, {
                'label': '访谈完成率(上个月)',
                'value': JobInterviewsData_month['job_interviews_completionRate'],
            }, {
                'label': '年度访谈人次',
                'value': JobInterviewsData_year['job_interviews_number'],
            },
        ]
        self.return_data['data']['big_card']['JobInterviews'] = {
            'title': "在职访谈",
            'tip': "",
            'btns': data
        }

    # 座談會
    def Colloquium(self):
        ColloquiumData_year = Colloquium.objects.filter(colloquium_base_id__in=self.user_base,
                                                        coll_interviews_status=1,
                                                        colloquium_date__year=self.now[0:4]).values(
            'colloquium_numberParticipants').aggregate(
            colloquium_numberParticipants=Sum("colloquium_numberParticipants")
        )
        ColloquiumData_month = Colloquium.objects.filter(colloquium_base_id__in=self.user_base,
                                                         coll_interviews_status=1,
                                                         colloquium_date__year=self.now[0:4],
                                                         colloquium_date__month=self.last_month[5:7]).values(
            'colloquium_numberParticipants', "colloquium_closeItem", "colloquium_outputItems").aggregate(
            colloquium_numberParticipants=Sum("colloquium_numberParticipants"),
            colloquium_closeItem=Sum("colloquium_closeItem"),
            colloquium_outputItems=Sum("colloquium_outputItems")
        )
        ColloquiumData_month = self.judge_number(ColloquiumData_month)
        ColloquiumData_year = self.judge_number(ColloquiumData_year)
        if ColloquiumData_month['colloquium_outputItems'] == 0:
            ColloquiumData_month['colloquium_completionRate'] = '0%'
        else:
            ColloquiumData_month['colloquium_completionRate'] = str(int(round(
                ColloquiumData_month['colloquium_closeItem'] / ColloquiumData_month[
                    'colloquium_outputItems'], 2) * 100)) + '%'
        data = [
            {
                'label': '座谈会参与人次(上个月)',
                'value': ColloquiumData_month['colloquium_numberParticipants']
            }, {
                'label': '座谈会完成率(上个月)',
                'value': ColloquiumData_month['colloquium_completionRate'],
            }, {
                'label': '年度访谈人次',
                'value': ColloquiumData_year['colloquium_numberParticipants']
            },
        ]
        self.return_data['data']['big_card']['Colloquium'] = {
            'title': "座谈会",
            'tip': "",
            'btns': data
        }

    # 离职访谈
    def ExitInterviews(self):
        ExitInterviewsData_year = ExitInterviews.objects.filter(
            exit_interviews_base_id__in=self.user_base,
            exit_interviews_status=1,
            exit_interviews_date__year=self.now[0:4]).values("exit_interviews_numberInterviews",
                                                             "exit_interviews_retentionSuccess").aggregate(
            exit_interviews_retentionSuccess=Sum("exit_interviews_retentionSuccess"))
        ExitInterviewsData_month = ExitInterviews.objects.filter(
            exit_interviews_base_id__in=self.user_base,
            exit_interviews_status=1,
            exit_interviews_date__year=self.now[0:4],
            exit_interviews_date__month=self.now[5:7],
        ).values("exit_interviews_numberInterviews", "exit_interviews_retentionSuccess").aggregate(
            exit_interviews_numberInterviews=Sum("exit_interviews_numberInterviews"),
            exit_interviews_retentionSuccess=Sum("exit_interviews_retentionSuccess")
        )
        ExitInterviewsData_year = self.judge_number(ExitInterviewsData_year)
        ExitInterviewsData_month = self.judge_number(ExitInterviewsData_month)
        if ExitInterviewsData_month['exit_interviews_retentionSuccess'] == 0:
            ExitInterviewsData_month['exit_interviews_retentionSuccessRate'] = '0%'
        else:
            ExitInterviewsData_month['exit_interviews_retentionSuccessRate'] = str(int(round(
                ExitInterviewsData_month['exit_interviews_retentionSuccess'] / ExitInterviewsData_month[
                    'exit_interviews_numberInterviews'], 2) * 100)) + '%'
        data = [
            {
                'label': '离职访谈人次(上个月)',
                'value': ExitInterviewsData_month['exit_interviews_numberInterviews']
            }, {
                'label': '挽留成功人次(上个月)',
                'value': ExitInterviewsData_month['exit_interviews_retentionSuccess'],
            }, {
                'label': '挽留成功率(上个月)',
                'value': ExitInterviewsData_month['exit_interviews_retentionSuccessRate'],
            }, {
                'label': '年度挽留成功人次',
                'value': ExitInterviewsData_year['exit_interviews_retentionSuccess']
            },
        ]
        self.return_data['data']['big_card']['ExitInterviews'] = {
            'title': "离职访谈",
            'tip': "",
            'btns': data
        }

    def TalentSubsidies(self):
        # 人才补贴
        TalentSubsidiesData_year = TalentSubsidies.objects.filter(
            talent_subsidies_base_id__in=self.user_base,
            talent_subsidies_status=1,
            talent_subsidies_date__year=self.now[0:4],
        ).values("talent_subsidies_claimed").aggregate(
            talent_subsidies_claimed=Sum("talent_subsidies_claimed"),
        )
        TalentSubsidiesData_month = TalentSubsidies.objects.filter(
            talent_subsidies_base_id__in=self.user_base,
            talent_subsidies_status=1,
            talent_subsidies_date__year=self.now[0:4],
            talent_subsidies_date__month=self.now[5:7],
        ).values("talent_subsidies_conditions", "talent_subsidies_applied", "talent_subsidies_claimed").aggregate(
            talent_subsidies_conditions=Sum("talent_subsidies_conditions"),
            talent_subsidies_applied=Sum("talent_subsidies_applied"),
            talent_subsidies_claimed=Sum("talent_subsidies_claimed"),
        )
        TalentSubsidiesData_month = self.judge_number(TalentSubsidiesData_month)
        TalentSubsidiesData_year = self.judge_number(TalentSubsidiesData_year)
        data = [
            {
                'label': '满足条件HC(上个月)',
                'value': TalentSubsidiesData_month['talent_subsidies_conditions']
            }, {
                'label': '已申请HC(上个月)',
                'value': TalentSubsidiesData_month['talent_subsidies_applied'],
            }, {
                'label': '已领取HC(上个月)',
                'value': TalentSubsidiesData_month['talent_subsidies_claimed'],
            }, {
                'label': '年度已领取HC数量',
                'value': TalentSubsidiesData_year['talent_subsidies_claimed'],
            },
        ]
        self.return_data['data']['big_card']['TalentSubsidies'] = {
            'title': "人才补贴",
            'tip': "",
            'btns': data
        }

    # 员工稽查
    def employeeInspect(self):
        employeeInspectData_year = EmployeeInspect.objects.filter(
            employee_inspect_base_id__in=self.user_base,
            employee_inspect_status=1,
            employee_inspect_date__year=self.now[0:4],
        ).values("employee_inspect_day_shift_no", "employee_inspect_night_shift_no").aggregate(
            employee_inspect_day_shift_no=Sum("employee_inspect_day_shift_no"),
            employee_inspect_night_shift_no=Sum("employee_inspect_night_shift_no")
        )
        employeeInspectData_month = EmployeeInspect.objects.filter(
            employee_inspect_base_id__in=self.user_base,
            employee_inspect_status=1,
            employee_inspect_date__year=self.now[0:4],
            employee_inspect_date__month=self.now[5:7],
        ).values("employee_inspect_day_shift_no", "employee_inspect_night_shift_no").aggregate(
            employee_inspect_day_shift_no=Sum("employee_inspect_day_shift_no"),
            employee_inspect_night_shift_no=Sum("employee_inspect_night_shift_no")
        )
        employeeInspectData_month = self.judge_number(employeeInspectData_month)
        employeeInspectData_year = self.judge_number(employeeInspectData_year)
        data = {
            'employeeInspectData': {
                "year": [
                    employeeInspectData_year['employee_inspect_day_shift_no'],
                    employeeInspectData_year['employee_inspect_night_shift_no'],
                ],
                "month": [
                    employeeInspectData_month['employee_inspect_day_shift_no'],
                    employeeInspectData_month['employee_inspect_night_shift_no'],
                ]
            },
        }
        data = [
            {
                'label': '白班稽核次数(本月)',
                'value': employeeInspectData_month['employee_inspect_day_shift_no'],
            }, {
                'label': '夜班稽核次数(本月)',
                'value': employeeInspectData_month['employee_inspect_night_shift_no'],
            }, {
                'label': '白班稽核(年)',
                'value': employeeInspectData_year['employee_inspect_day_shift_no'],
            }, {
                'label': '夜班稽核(年)',
                'value': employeeInspectData_year['employee_inspect_night_shift_no'],
            },
        ]
        self.return_data['data']['big_card']['employeeInspect'] = {
            'title': "员工稽查",
            'tip': "",
            'btns': data
        }

    def recruit_data(self):
        nav_list = {
            45: self.dl,
            46: self.idl,
            47: self.sal,
            50: self.salarySurvey,
            57: self.MemorabiliaList,
            59: self.externalHonorsList,
            61: self.InternalEvaluationList,
            63: self.employeeActivitiesList,
            65: self.ProjectBonus,
            66: self.RewardsAndPunishments,
            68: self.JobInterviews,
            69: self.Colloquium,
            70: self.ExitInterviews,
            71: self.TalentSubsidies,
            73: self.employeeInspect
        }
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功',
            'path': [],
            'data': {
                'small_card': [],
                'big_card': {}
            }
        }
        obj = AdminUser.objects.filter(pk=self.token).values_list("user_menu")
        menu_id = [i[0] for i in obj]

        nav_obj = AdminNavMenuList.objects.filter(pk__in=menu_id, nav_parent_id__isnull=True).values("id", "nav_url")
        nav_obj = [i for i in nav_obj]
        path = []
        for nav in nav_obj:
            try:
                # print(nav)
                child_nav = AdminNavMenuList.objects.filter(pk__in=menu_id, nav_parent_id=nav['id']).values("nav_url")[0]
                path.append(nav['nav_url'] + child_nav['nav_url'])
            except KeyError:
                pass
        self.return_data['path'] = path
        for i in menu_id:
            if i in nav_list.keys():
                nav_list[i]()

    def judge_number(self, data_dict):
        if isinstance(data_dict, dict):
            for key, value in data_dict.items():
                if isinstance(value, int) is False:
                    data_dict[key] = 0

        return data_dict
