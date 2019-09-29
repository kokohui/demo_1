# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AppAnaStarlevel(models.Model):
    commodity_all = models.CharField(max_length=15)
    commodity_one = models.CharField(max_length=15)
    commodity_two = models.CharField(max_length=15)
    commodity_three = models.CharField(max_length=15)
    commodity_four = models.CharField(max_length=15)
    commodity_five = models.CharField(max_length=15)
    comm_pro_one = models.CharField(max_length=10)
    comm_pro_two = models.CharField(max_length=10)
    comm_pro_three = models.CharField(max_length=10)
    comm_pro_four = models.CharField(max_length=10)
    comm_pro_five = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'app_ana_starlevel'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BusProd(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    eva_num = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    percent_rate = models.CharField(max_length=255, blank=True, null=True)
    pro_url = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    keep_time = models.CharField(max_length=255, blank=True, null=True)
    shop_size = models.CharField(max_length=255, blank=True, null=True)
    seller_key = models.CharField(max_length=255, blank=True, null=True)
    shop_rating = models.CharField(max_length=255, blank=True, null=True)
    con_home_url = models.CharField(max_length=255, blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    discount = models.CharField(max_length=255, blank=True, null=True)
    class_info = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_del = models.CharField(max_length=1, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    item_ana_json = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_prod'


class BusStar(models.Model):
    create_by = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_del = models.CharField(max_length=1, blank=True, null=True)
    json = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_star'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SysArea(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    alias = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    subsite_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_area'


class SysCity(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    pid = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    areaid = models.CharField(max_length=100, blank=True, null=True)
    is_open = models.CharField(max_length=10, blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_del = models.CharField(max_length=255, blank=True, null=True)
    is_vr_pc_top = models.CharField(max_length=1, blank=True, null=True)
    is_vr_are_top = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_city'


class SysDict(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    sort = models.CharField(max_length=255)
    create_by = models.CharField(max_length=255)
    create_date = models.DateField()
    is_del = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_enable = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sys_dict'


class SysFile(models.Model):
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.CharField(max_length=255, blank=True, null=True)
    file_suffix = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    is_del = models.CharField(max_length=255, blank=True, null=True)
    old_name = models.CharField(max_length=255, blank=True, null=True)
    gt_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_file'


class SysMenu(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    menuto = models.CharField(max_length=60, blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    is_del = models.CharField(max_length=255, blank=True, null=True)
    pid = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    href = models.CharField(max_length=255, blank=True, null=True)
    permission = models.TextField(blank=True, null=True)
    is_show = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    miaoshu = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    open_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_menu'


class SysMenusTo(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    is_del = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    is_show = models.CharField(max_length=1, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    is_platform = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_menus_to'


class SysMoblieCode(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    moblie = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_del = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_moblie_code'


class SysRole(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    role_ename = models.CharField(max_length=255)
    is_enable = models.CharField(max_length=100)
    create_by = models.CharField(max_length=255)
    create_date = models.DateField()
    is_del = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleMenu(models.Model):
    role_id = models.CharField(max_length=100)
    menu_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sys_role_menu'


class SysUser(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    login_name = models.CharField(max_length=100, blank=True, null=True)
    is_del = models.CharField(max_length=255, blank=True, null=True)
    is_enable = models.CharField(max_length=32, blank=True, null=True)
    customer_type = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    service_qq = models.CharField(max_length=20, blank=True, null=True)
    service_tel = models.CharField(max_length=20, blank=True, null=True)
    pass_str = models.CharField(max_length=255, blank=True, null=True)
    linkman = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    channel_open_id = models.CharField(max_length=255, blank=True, null=True)
    channel_duty_id = models.CharField(max_length=255, blank=True, null=True)
    service_id = models.CharField(max_length=255, blank=True, null=True)
    rebate_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    channel_level = models.IntegerField(blank=True, null=True)
    weichat_no = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    channel_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserAddress(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_del = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_address'


class SysUserLog(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    is_del = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_log'


class SysUserRole(models.Model):
    user_id = models.CharField(max_length=255)
    role_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sys_user_role'


class SystemProvinceCity(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    parentid = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    areaid = models.CharField(max_length=100, blank=True, null=True)
    isopen = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    is_del = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_province_city'
