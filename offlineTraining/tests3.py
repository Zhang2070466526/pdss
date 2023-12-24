# # sql_query = """
# #             SELECT
# #                 IFNULL(dc.department_first_name, 'Total') AS base_name,
# #                 IFNULL(cat.category_name, 'Total') AS category_name,
# #                 IFNULL(lvl.level_name, 'Total') AS level_name,
# #                 COALESCE(COUNT(tc.id), 0) AS count,
# #                 COALESCE(SUM(tc.content_people_number), 0) AS total_people,
# #                 COALESCE(SUM(tc.content_duration), 0) AS total_duration,
# #                 COALESCE(SUM(tc.content_satisfaction), 0) AS total_satisfaction,
# #                 CASE WHEN SUM(tc.content_people_number) > 0 THEN
# #                     COALESCE(SUM(tc.content_satisfaction) / SUM(tc.content_people_number), 0)
# #                 ELSE
# #                     0
# #                 END AS avg_satisfaction
# #             FROM (
# #                 SELECT id, department_first_name
# #                 FROM hr_department
# #                 WHERE department_first_name IS NOT NULL
# #                   AND (department_expiry_date IS NULL OR department_expiry_date >= NOW())
# #             ) dc
# #             CROSS JOIN
# #                 training_content_category cat
# #             CROSS JOIN
# #                 training_content_level lvl
# #             LEFT JOIN (
# #                 SELECT *
# #                 FROM training_content
# # 		WHERE content_end_date >= DATE_FORMAT( '{}', '%Y-%m-01 00:00:00' )
# # 		AND content_end_date <= LAST_DAY( '{}' ) + INTERVAL 1 DAY - INTERVAL 1 SECOND
# #             ) tc ON tc.content_part_id = dc.id
# #                   AND tc.content_category_id = cat.id
# #                   AND tc.content_level_id = lvl.id
# #             GROUP BY
# #                 dc.department_first_name, cat.category_name, lvl.level_name
# #             WITH ROLLUP;
# #
# #         """.format('2023-08-01','2023-08-31')
# # print(sql_query)
#
#
# # a='D:\Runergy_SourceCode\Python\pdss\static\offlineTrainingFile\download_file\2023-08-30\1693354345.366526\线下培训汇总分析.xlsx'
# # print(a.split('static\\'))
#
#
#
#
#
#
#
#
# # class HrEmployee(models.Model):
# #     employee_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')
# #     employee_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='工号')
# #     employee_job_rank = models.ForeignKey(to=HrJobRank, on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,
# #                                           verbose_name='合同归属')
#
#
# # # print(current_month,next_month)
# # first_level_departments = HrDepartment.objects.filter(~Q(id=999999),
# #     Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gt=datetime.now()),department_first_name__isnull=False,
# #     department_status=1
# #     ).values('department_first_name').annotate(
# #     total_onsite_duration=Sum('trainingcontent__content_duration',
# #                               filter=Q(trainingcontent__content_manner='现场') &
# #                                      Q(trainingcontent__content_begin_date__gte=current_month) &
# #                                      Q(trainingcontent__content_end_date__lte=next_month)&
# #                                      Q(trainingcontent__content_status=1)
# #                                      )
# # )
# # for department in first_level_departments:
# #     if department['total_onsite_duration'] is None:
# #         department['total_onsite_duration'] = 0
# #
# #
# # # from django.db.models import Count, Sum, F
# # # result = TrainingContent.objects.filter(content_manner='现场') \
# # #     .values('content_part__department_first_name') \
# # #     .annotate(count_content_part=Count('content_part__department_first_name'),
# # #               sum_people_number=Sum(F('content_people_number'))) \
# # #     .order_by('content_part__department_first_name')
# # #
# # # # Print the results
# # # for item in result:
# # #     print(f"Department: {item['content_part__department_first_name']}")
# # #     print(f"Count of content_part: {item['count_content_part']}")
# # #     print(f"Sum of content_people_number: {item['sum_people_number']}")
# #
# # from django.db.models import Sum
# # from datetime import datetime
# # from django.db.models import Q
# #
# # # Assuming your TrainingContent model and HrDepartment model are imported correctly.
# #
# # # Perform the aggregation query with additional constraints
# # result = TrainingContent.objects.filter(
# #     Q(content_manner='现场') &
# #     Q(content_begin_date__gte=current_month) &
# #     Q(content_end_date__lte=next_month) &
# #     Q(content_status=1)
# # ).values('content_part__department_first_name') \
# #     .annotate(total_people=Sum('content_people_number')) \
# #     .filter(
# #     Q(content_part__department_expiry_date__isnull=True)
# #                                                  | Q(content_part__department_expiry_date__gt=datetime.now()),
# #     content_part__department_status=1
# # )
# #
# # # Iterate through the result to print the department names and total people for each department
# # for people in result:
# #     for hour in first_level_departments:
# #         if people['content_part__department_first_name']==hour['department_first_name']:
# #             print(people['total_people'],hour['total_onsite_duration'])
# #             hour['total_onsite_duration']=round(people['total_people']*hour['total_onsite_duration'],2)
# # print(first_level_departments)
# #     # print(item)
# # # for item in result:
# # #     department_name = item['content_part__department_first_name']
# # #     total_people = item['total_people']
# # #     print(f"Department: {department_name}, Total People: {total_people}")
# #
# # for department in first_level_departments:
# #     sessionInfo={
# #         "sessions_base": department['department_first_name'],
# #         'sessions_offline_total':department['total_onsite_duration'],
# #         'sessions_record_time':str(current_month)[:10]
# #     }
# #     TrainingSessions.objects.update_or_create(defaults=sessionInfo,sessions_base=sessionInfo['sessions_base'],sessions_record_time=sessionInfo['sessions_record_time'])
#
# # from django.db.models import Sum, F, ExpressionWrapper, FloatField, Q
# # from django.db.models.functions import Coalesce
# # from datetime import datetime
# #
# # # Define an ExpressionWrapper to calculate the product of content_duration and content_people_number
# # product_expression = ExpressionWrapper(
# #     F('content_duration') * F('content_people_number'),
# #     output_field=FloatField()
# # )
# #
# # # Create a queryset that filters for content_manner '现场' and aggregates the sum of the product by department_first_name
# # print(current_month,next_month)
# # result = (
# #     TrainingContent.objects.filter(
# #         Q(content_manner='现场') &
# #         (
# #                 Q(content_part__department_expiry_date__isnull=True) |
# #                 Q(content_part__department_expiry_date__gt=datetime.now())|
# #                 Q(content_part__department_first_name__isnull=False)|
# #                 Q(content_part__department_status=1)
# #         ) &
# #         Q(content_part__department_status=1)&
# #     Q(content_begin_date__gte=current_month) &
# #     Q(content_end_date__lte=next_month)
# #     )
# #     .annotate(product=product_expression)
# #     .values('content_part__department_first_name')
# #     .annotate(total=Sum('product'))
# #     .values('content_part__department_first_name', 'total')
# # )
#
#
#
#
#
a=[
  {
    'department': '全球战略供应链管理中心',
    'category': '知识类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球战略供应链管理中心',
    'category': '技能类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球战略供应链管理中心',
    'category': '态度类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球战略供应链管理中心',
    'category': '合计',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球组件营销中心',
    'category': '知识类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球组件营销中心',
    'category': '技能类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球组件营销中心',
    'category': '态度类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球组件营销中心',
    'category': '合计',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '光伏研究院',
    'category': '知识类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '光伏研究院',
    'category': '技能类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '光伏研究院',
    'category': '态度类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '光伏研究院',
    'category': '合计',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  }]

b=[
  {
    'department': '全球战略供应链管理中心',
    'category': '知识类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球战略供应链管理中心',
    'category': '技能类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球战略供应链管理中心',
    'category': '态度类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球战略供应链管理中心',
    'category': '合计',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球组件营销中心',
    'category': '知识类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球组件营销中心',
    'category': '技能类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球组件营销中心',
    'category': '态度类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '全球组件营销中心',
    'category': '合计',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },

    {
    'department': '润阳集团',
    'category': '知识类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '润阳集团',
    'category': '技能类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '润阳集团',
    'category': '态度类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '润阳集团',
    'category': '合计',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0.0,
    'content_duration': 0.0,
    'content_satisfaction': 0,
    'content_satisfaction_avg': 0.0,
    'content_number_Total': '0',
    'content_number_middle': '0',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },]

# count_dict=[]
# for line in a:
#     # print(line)
#     count_dict_zhishi={'count_null_Satisfaction_Total':0}
#     count_dict_jineng = {}
#     count_dict_taidu = {}
#     count_dict_heji = {}
#     if line['category']=='知识类':
#         count_dict_zhishi['count_null_Satisfaction_Total']+=float(count_dict_zhishi['count_null_Satisfaction_Total'])
#         count_dict_zhishi['content_people_number'] += float(count_dict_zhishi['content_people_number'])
#         # count_dict_zhishi['content_duration'] += float(count_dict_zhishi['content_duration'])
#         # count_dict_zhishi['content_satisfaction'] += float(count_dict_zhishi['content_satisfaction'])
#         #
#         # count_dict_zhishi['content_satisfaction_avg']+=float(count_dict_zhishi['content_satisfaction_avg'])
#         # count_dict_zhishi['content_number_Total'] += float(count_dict_zhishi['content_number_Total'])
#         # count_dict_zhishi['content_number_middle'] += float(count_dict_zhishi['content_number_middle'])
#         # count_dict_zhishi['content_number_grass'] += float(count_dict_zhishi['content_number_grass'])
#         # count_dict_zhishi['content_number_synthesis'] += float(count_dict_zhishi['content_number_synthesis'])
#         # count_dict_zhishi['content_number_senior'] += float(count_dict_zhishi['content_number_senior'])
#         count_dict_zhishi={
#             'department':'润阳集团',
#             'category':'知识类',
#         }
#         count_dict.append(count_dict_zhishi)
#
#
# print(count_dict)


a=[ {
    'department': '组件事业部',
    'category': '知识类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 469.0,
    'content_duration': 46.5,
    'content_satisfaction': 91.2,
    'content_satisfaction_avg': 91.2,
    'content_number_Total': '15',
    'content_number_middle': '0',
    'content_number_grass': '4',
    'content_number_synthesis': '11',
    'content_number_senior': '0'
  },
  {
    'department': '组件事业部',
    'category': '技能类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 859.0,
    'content_duration': 103.0,
    'content_satisfaction': 39.41,
    'content_satisfaction_avg': 39.41,
    'content_number_Total': '57',
    'content_number_middle': '0',
    'content_number_grass': '31',
    'content_number_synthesis': '26',
    'content_number_senior': '0'
  },
  {
    'department': '组件事业部',
    'category': '态度类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 19.0,
    'content_duration': 2.0,
    'content_satisfaction': 95.2,
    'content_satisfaction_avg': 95.2,
    'content_number_Total': '1',
    'content_number_middle': '1',
    'content_number_grass': '0',
    'content_number_synthesis': '0',
    'content_number_senior': '0'
  },
  {
    'department': '组件事业部',
    'category': '合计',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 1347.0,
    'content_duration': 151.5,
    'content_satisfaction': 50.82,
    'content_satisfaction_avg': 50.82,
    'content_number_Total': '73',
    'content_number_middle': '1',
    'content_number_grass': '35',
    'content_number_synthesis': '37',
    'content_number_senior': '0'
  },
  {
    'department': '硅料事业部',
    'category': '知识类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 1300.0,
    'content_duration': 55.5,
    'content_satisfaction': 97.49,
    'content_satisfaction_avg': 97.49,
    'content_number_Total': '49',
    'content_number_middle': '0',
    'content_number_grass': '27',
    'content_number_synthesis': '22',
    'content_number_senior': '0'
  },
  {
    'department': '硅料事业部',
    'category': '技能类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 492.0,
    'content_duration': 37.0,
    'content_satisfaction': 97.44,
    'content_satisfaction_avg': 97.44,
    'content_number_Total': '25',
    'content_number_middle': '0',
    'content_number_grass': '17',
    'content_number_synthesis': '8',
    'content_number_senior': '0'
  },
  {
    'department': '硅料事业部',
    'category': '态度类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 496.0,
    'content_duration': 261.0,
    'content_satisfaction': 97.62,
    'content_satisfaction_avg': 97.62,
    'content_number_Total': '8',
    'content_number_middle': '0',
    'content_number_grass': '2',
    'content_number_synthesis': '6',
    'content_number_senior': '0'
  },
  {
    'department': '硅料事业部',
    'category': '合计',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 2288.0,
    'content_duration': 353.5,
    'content_satisfaction': 97.49,
    'content_satisfaction_avg': 97.49,
    'content_number_Total': '82',
    'content_number_middle': '0',
    'content_number_grass': '46',
    'content_number_synthesis': '36',
    'content_number_senior': '0'
  }]


zz=  [{
    'department': '润阳集团',
    'category': '知识类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0,
    'content_duration': 0,
    'content_satisfaction': 0,
    'content_satisfaction_avg':0,
    'content_number_Total': 0,
    'content_number_middle': 0,
    'content_number_grass': 0,
    'content_number_synthesis': 0,
    'content_number_senior': 0
  },
  {
    'department': '润阳集团',
    'category': '技能类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0,
    'content_duration': 0,
    'content_satisfaction': 0,
    'content_satisfaction_avg':0,
    'content_number_Total': 0,
    'content_number_middle': 0,
    'content_number_grass': 0,
    'content_number_synthesis': 0,
    'content_number_senior': 0
  },
  {
    'department': '润阳集团',
    'category': '态度类',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0,
    'content_duration': 0,
    'content_satisfaction': 0,
    'content_satisfaction_avg':0,
    'content_number_Total': 0,
    'content_number_middle': 0,
    'content_number_grass': 0,
    'content_number_synthesis': 0,
    'content_number_senior': 0
  },
  {
    'department': '润阳集团',
    'category': '合计',
    'count_null_Satisfaction_Total': 0,
    'content_people_number': 0,
    'content_duration': 0,
    'content_satisfaction': 0,
    'content_satisfaction_avg':0,
    'content_number_Total': 0,
    'content_number_middle': 0,
    'content_number_grass': 0,
    'content_number_synthesis': 0,
    'content_number_senior': 0
  }]


# # 创建一个字典用于存储不同部门和类别的总和
# department_category_totals = {}
# data=a
# for entry in data:
#     department = entry['department']
#     category = entry['category']
#     content_people_number = entry['content_people_number']
#
#     # 初始化部门和类别的总和字典条目
#     if (department, category) not in department_category_totals:
#         department_category_totals[(department, category)] = {
#             'content_people_number': 0
#         }
#
#     # 累加 'content_people_number'
#     department_category_totals[(department, category)]['content_people_number'] += content_people_number
#
# # 创建润阳集团的初始数据
# ruyang_data = []
#
# # 遍历字典中的项，根据不同的部门和类别动态创建数据
# for (department, category), totals in department_category_totals.items():
#     ruyang_entry = {
#         'department': '润阳集团',
#         'category': category,
#         'count_null_Satisfaction_Total': 0,
#         'content_people_number': totals['content_people_number'],
#         'content_duration': 0,  # 这里需要根据您的需求进行设置
#         'content_satisfaction': 0,  # 这里需要根据您的需求进行设置
#         'content_satisfaction_avg': 0,  # 这里需要根据您的需求进行设置
#         'content_number_Total': 0,  # 这里需要根据您的需求进行设置
#         'content_number_middle': 0,  # 这里需要根据您的需求进行设置
#         'content_number_grass': 0,  # 这里需要根据您的需求进行设置
#         'content_number_synthesis': 0,  # 这里需要根据您的需求进行设置
#         'content_number_senior': 0  # 这里需要根据您的需求进行设置
#     }
#     ruyang_data.append(ruyang_entry)
#
# # 将润阳集团的数据添加到总和字典中
# for entry in ruyang_data:
#     department = entry['department']
#     category = entry['category']
#     content_people_number = entry['content_people_number']
#
#     if (department, category) not in department_category_totals:
#         department_category_totals[(department, category)] = {
#             'content_people_number': 0
#         }
#
#     department_category_totals[(department, category)]['content_people_number'] += content_people_number
#
# # 将结果转化为列表形式
# zz = [{'department': department, 'category': category, **totals}
#       for (department, category), totals in department_category_totals.items()]
#
# # 打印 zz
# for entry in zz:
#     print(entry)



tttt=[]
# 创建一个字典用于存储不同部门和类别的总和
department_category_totals = {}
data=a
for entry in data:
    department = entry['department']
    category = entry['category']
    count_null_Satisfaction_Total = entry['count_null_Satisfaction_Total']
    content_duration = entry['content_duration']
    content_satisfaction = entry['content_satisfaction']
    content_satisfaction_avg = entry['content_satisfaction_avg']
    content_people_number = entry['content_people_number']
    content_number_Total = float(entry['content_number_Total'])
    content_number_middle = float(entry['content_number_middle'])
    content_number_grass = float(entry['content_number_grass'])
    content_number_synthesis = float(entry['content_number_synthesis'])
    content_number_senior = float(entry['content_number_senior'])

    # 初始化部门和类别的总和字典条目
    if (department, category) not in department_category_totals:
        department_category_totals[(department, category)] = {
            'count_null_Satisfaction_Total': 0,
            'content_duration': 0,
          'content_people_number':0,
            'content_satisfaction': 0,
            'content_satisfaction_avg': 0,
            'content_number_Total': 0,
            'content_number_middle': 0,
            'content_number_grass': 0,
            'content_number_synthesis': 0,
            'content_number_senior': 0
        }

    # 累加各个指标
    department_category_totals[(department, category)]['count_null_Satisfaction_Total'] += count_null_Satisfaction_Total
    department_category_totals[(department, category)]['content_duration'] += content_duration
    department_category_totals[(department, category)]['content_people_number'] += content_people_number
    department_category_totals[(department, category)]['content_satisfaction'] += content_satisfaction
    department_category_totals[(department, category)]['content_satisfaction_avg'] += content_satisfaction_avg
    department_category_totals[(department, category)]['content_number_Total'] += content_number_Total
    department_category_totals[(department, category)]['content_number_middle'] += content_number_middle
    department_category_totals[(department, category)]['content_number_grass'] += content_number_grass
    department_category_totals[(department, category)]['content_number_synthesis'] += content_number_synthesis
    department_category_totals[(department, category)]['content_number_senior'] += content_number_senior

# 创建润阳集团的初始数据
ruyang_data = []

# 遍历字典中的项，根据不同的部门和类别动态创建数据
for (department, category), totals in department_category_totals.items():
    ruyang_entry = {
        'department': '润阳集团',
        'category': category,
        'count_null_Satisfaction_Total': totals['count_null_Satisfaction_Total'],
        'content_duration': totals['content_duration'],
        'content_satisfaction': totals['content_satisfaction'],
        'content_satisfaction_avg': totals['content_satisfaction_avg'],
        'content_number_Total': totals['content_number_Total'],
        'content_number_middle': totals['content_number_middle'],
        'content_number_grass': totals['content_number_grass'],
        'content_number_synthesis': totals['content_number_synthesis'],
        'content_number_senior': totals['content_number_senior'],
      'content_people_number':totals['content_people_number']
    }
    ruyang_data.append(ruyang_entry)

# 将润阳集团的数据添加到总和字典中
for entry in ruyang_data:
    department = entry['department']
    category = entry['category']
    count_null_Satisfaction_Total = entry['count_null_Satisfaction_Total']
    content_duration = entry['content_duration']
    content_satisfaction = entry['content_satisfaction']
    content_satisfaction_avg = entry['content_satisfaction_avg']
    content_number_Total = entry['content_number_Total']
    content_number_middle = entry['content_number_middle']
    content_number_grass = entry['content_number_grass']
    content_number_synthesis = entry['content_number_synthesis']
    content_number_senior = entry['content_number_senior']
    content_people_number=entry['content_people_number']

    if (department, category) not in department_category_totals:
        department_category_totals[(department, category)] = {
            'count_null_Satisfaction_Total': 0,
            'content_duration': 0,
            'content_satisfaction': 0,
            'content_satisfaction_avg': 0,
            'content_number_Total': 0,
            'content_number_middle': 0,
            'content_number_grass': 0,
            'content_number_synthesis': 0,
            'content_number_senior': 0,
          'content_people_number':0
        }

    department_category_totals[(department, category)]['count_null_Satisfaction_Total'] += count_null_Satisfaction_Total
    department_category_totals[(department, category)]['content_people_number'] += content_people_number
    department_category_totals[(department, category)]['content_duration'] += content_duration
    department_category_totals[(department, category)]['content_satisfaction'] += content_satisfaction
    department_category_totals[(department, category)]['content_satisfaction_avg'] += content_satisfaction_avg
    department_category_totals[(department, category)]['content_number_Total'] += content_number_Total
    department_category_totals[(department, category)]['content_number_middle'] += content_number_middle
    department_category_totals[(department, category)]['content_number_grass'] += content_number_grass
    department_category_totals[(department, category)]['content_number_synthesis'] += content_number_synthesis
    department_category_totals[(department, category)]['content_number_senior'] += content_number_senior

# 将结果转化为列表形式
zz = [{'department': department, 'category': category, **totals}
      for (department, category), totals in department_category_totals.items()]

# 打印 zz
for entry in zz:
    print(entry)
    tttt.append(entry)
print()
print(a)
print(tttt)
second_name_list = ['江苏润阳悦达光伏科技有限公司', '润阳泰国四期电池', '江苏润阳世纪光伏科技有限公司',
                    '江苏润阳光伏科技有限公司', '江苏海博瑞光伏科技有限公司', '江苏润宝电力科技有限公司',
                    '润阳泰国四期组件', '云南润阳世纪光伏科技有限公司', '宁夏润阳硅材料科技有限公司',
                    '润阳光伏科技（泰国）有限公司'],


first_name_list=['光伏研究院','战略采购中心','全球财务中心','人力资源中心']



# [
#   {
#     'department': '润阳集团',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0,
#     'content_satisfaction_avg': 0,
#     'content_number_Total': 0.0,
#     'content_number_middle': 0.0,
#     'content_number_grass': 0.0,
#     'content_number_synthesis': 0.0,
#     'content_number_senior': 0.0,
#     'content_people_number': 0.0
#   },
#   {
#     'department': '润阳集团',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0,
#     'content_satisfaction_avg': 0,
#     'content_number_Total': 0.0,
#     'content_number_middle': 0.0,
#     'content_number_grass': 0.0,
#     'content_number_synthesis': 0.0,
#     'content_number_senior': 0.0,
#     'content_people_number': 0.0
#   }] 将字典排序 按照                    'content_number_senior'
#                     'content_number_middle'
#                     'content_number_grass'
#                     'content_number_synthesis'
#                     'content_number_Total'
#                     'content_people_number'
#                     'content_duration'
#                     'content_satisfaction'
#                     'content_satisfaction_avg'
#                     'count_null_Satisfaction_Total'排列


# 定义两个列表
# 定义两个列表
list1 = [339, 339, 339, 32, 33, 32, 32, 32, 32, 1, 339, 31, 294, 369, 369, 32, 32, 32, 32, 369, 369, 369, 369, 369, 369, 369, 369, 369, 33, 33, 33, 33, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32]
list2 = [31, 32, 33, 77, 167, 237, 238, 239, 292, 339, 340, 358, 369, 370, 408, 409, 410, 411, 413, 524, 525, 526, 527, 528, 529, 530, 531, 532, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 670]

# 找到不同的节点
different_nodes = [node for node in list1 if node not in list2] + [node for node in list2 if node not in list1]

# 去重
different_nodes = list(set(different_nodes))

# 输出不同的节点
print(different_nodes)

