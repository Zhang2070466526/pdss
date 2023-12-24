from django.db import models


# python manage.py makemigrations auther
# python manage.py migrate auther


nav_type_choices = (
    (1, '路由'),
    (2, '功能按钮'),
    (3,'字段')
)

class AdminNavMenuList(models.Model):    #现在用的
    nav_index = models.CharField(max_length=50, null=True, blank=True, verbose_name='序号')
    nav_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='菜单名')
    nav_url = models.CharField(max_length=100, null=True, blank=True, verbose_name='路径')
    nav_icon = models.CharField(max_length=50, null=True, blank=True, verbose_name='图标')
    nav_component = models.CharField(max_length=100, null=True, blank=True, verbose_name='组件路径')
    nav_type = models.IntegerField(default=1, verbose_name='权限类型', choices=nav_type_choices)
    nav_parent_id = models.IntegerField(verbose_name='上级id', null=True, blank=True)
    nav_name_field = models.CharField(max_length=50,verbose_name='nav_name对应的field', null=True, blank=True)   #花名册
    # nav_first_order = models.CharField(max_length=50, null=True, blank=True)   #最外层菜单名称
    class Meta:
        managed = True
        db_table = 'admin_nav_menu_list'
        verbose_name_plural = '管理员平台导航菜单汇总表'
        verbose_name = '管理员平台导航菜单汇总表'

class AdminMenuNavList(models.Model):  #未来用的
    menu_index = models.CharField(max_length=50, null=True, blank=True, verbose_name='序号')
    menu_icon=models.CharField(max_length=255, null=True, blank=True, verbose_name='图标')
    menu_path=models.CharField(max_length=255, null=True, blank=True, verbose_name='路径')     #侧边栏路径
    menu_complete_path = models.CharField(max_length=255, null=True, blank=True, verbose_name='完整路径')   #导航路径
    menu_component = models.CharField(max_length=100, null=True, blank=True, verbose_name='组件路径')
    menu_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='导航名')
    menu_type = models.IntegerField(default=1, verbose_name='权限类型', choices=nav_type_choices)
    menu_parent_id = models.IntegerField(verbose_name='上级id', null=True, blank=True)
    menu_level=models.IntegerField(verbose_name='导航所属等级')
    menu_category_id = models.IntegerField(verbose_name='导航所属类别id')   #一级大类的id
    menu_category_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='所属类别名称')
    menu_secondary_category_id = models.IntegerField(verbose_name='二级导航id')  #二级类id
    # menu_flag= models.IntegerField(verbose_name='判断导航是否多层')   #1是单层,2是多层
    class Meta:
        managed = True
        db_table = 'admin_menu_nav_list'
        verbose_name_plural = '导航汇总表'
        verbose_name = '导航汇总表'



class AdminUser(models.Model):
    username = models.CharField(max_length=50, default='', verbose_name='登录名')  #工号
    password = models.CharField(max_length=255, default='', verbose_name='登录密码')
    user = models.CharField(max_length=50, default='', verbose_name='用户名')
    is_superuser = models.BooleanField(verbose_name='是否是管理员', default=False)
    is_used = models.BooleanField(verbose_name='是否启用', default=True)
    user_base = models.ManyToManyField(to='general.center_base', verbose_name='用户所在基地', related_name='user_base',db_constraint=False)
    user_jobrank = models.ManyToManyField(to='volumeContracts.ContractsJobrank', verbose_name='用户所在合同归属',related_name='user_jobrank', db_constraint=False)
    user_menu = models.ManyToManyField(to='AdminNavMenuList', verbose_name='用户权限', related_name='user_menu',db_constraint=False)   #侧边栏
    # user_jobrank_hik=models.ManyToManyField(to='hikCanteen.JobRank', verbose_name='用户所在合同归属(消费)', related_name='user_jobrank_hik',db_constraint=False)
    user_jobrank_employee=models.ManyToManyField(to='employee.HrJobRank', verbose_name='合同归属', related_name='user_jobrank_employee',db_constraint=False)
    user_department_employee = models.ManyToManyField(to='employee.HrDepartment', verbose_name='基地部门',related_name='user_department_employee', db_constraint=False)
    user_nav=models.ManyToManyField(to='AdminMenuNavList', verbose_name='用户导航权限', related_name='user_nav',db_constraint=False)    #导航
    # user_stationed_base= models.ManyToManyField(to='expatriateRecord.ImmigrationBase', verbose_name='派驻基地(出入境)',related_name='user_stationed_base', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    # user_remark = models.TextField(null=True,blank=True, verbose_name='备注')
    user_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')

    class Meta:
        managed = True
        db_table = 'admin_user'
        verbose_name_plural = '管理员平台用户表'
        verbose_name = '管理员平台用户表'








class UploadFiles(models.Model):
    file_name = models.CharField(max_length=255, default='', verbose_name='文件名')
    file_url = models.CharField(max_length=255, default='', verbose_name='文件路径')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    status = models.BooleanField(default=True, verbose_name='数据是否有效')

    class Meta:
        managed = True
        db_table = 'upload_files'
        verbose_name_plural = '上传文件表'
        verbose_name = '上传文件表'



# class AdminFieldList(models.Model):
#     field_index = models.CharField(max_length=50, null=True, blank=True, verbose_name='序号')
#     field_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='字段名')
#     field_menu = models.ForeignKey(to='AdminNavMenuList', on_delete=models.SET_NULL, null=True, blank=True,
#                                verbose_name='路由对应的字段', related_name='field_menu', db_constraint=False)
#     field_user= models.ForeignKey(to='AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                verbose_name='用户对应的字段', related_name='field_user', db_constraint=False)
#     field_status = models.BooleanField(default=True, verbose_name='数据是否有效')
#
#     class Meta:
#         managed = True
#         db_table = 'admin_field_list'
#         verbose_name_plural = '用户对应字段表'
#         verbose_name = '用户对应字段表'