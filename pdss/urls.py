"""
URL configuration for pdss project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('auther/', include("auther.urls")),
    path('salarySurvey/', include("salarySurvey.urls")),
    path('externalHonors/', include("externalHonors.urls")),
    path('general/', include("general.urls")),
    path('memorabilia/', include("memorabilia.urls")),    #公司大事记
    path('internalEvaluation/',include('internalEvaluation.urls')),#内部评优
    path('employeeInspect/',include('employeeInspect.urls')),#员工稽核
    path('rewardsPunishments/',include('rewardsPunishments.urls')),#奖惩
    path('employeeCare/',include('employeeCare.urls')),#员工关怀
    path('setup/',include('setup.urls')),
    path('employeeActivities/', include("employeeActivities.urls")),
    path('recruit/', include("recruit.urls")),
    # path('volumeContracts/',include('volumeContracts.urls'))#批量合同
    path('scanQrCode/', include('volumeContracts.urls')),  # 批量合同
    path('competeRestrictions/', include('competeRestrictions.urls')),  # 竞业限制
    path('hikCanteen/', include('hikCanteen.urls')),  #食堂消费
    path('rayongAttendance/', include('rayongAttendance.urls')) ,#泰国罗勇
    path('expatriate/', include("expatriateRecord.urls")),  #外派台账
    path('indexShow/', include("indexShow.urls")),
    path('employee/',include("employee.urls")),#员工入职
    path('offlineTraining/',include("offlineTraining.urls")),#线下培训
    path('ieProposal/',include('IeProposal.urls')),#IE提案
    path('socialSecurity/',include('socialSecurity.urls')),#员工社保平台
    path('performance/',include('performance.urls')),#绩效
    path('wx/',include('wx.urls')),#绩效
    path('shoeCabinet/', include('shoeCabinet.urls')),  # 衣鞋柜模块
    path('immigration/', include('expatriateRecord.immigration.urls')),  # 出入境管理
    path('employeePersonnel/', include('employeePersonnel.urls')),#员工人事数据
    path('testApp/',include('testApp.urls')),


    # path('staffFollowing/',include('staffFollowing.urls')),#人才发展
    path('talentDevelop/',include('talentDevelop.urls')),#人才发展

    # path('archives/', include('employee.archives.urls')),  # 档案管理



    # path('employeeActivities/', include("employeeActivities.urls")),
    # path('recruit/', include("recruit.urls")),

]
# from django.conf import settings
# from django.urls import path, include
# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))