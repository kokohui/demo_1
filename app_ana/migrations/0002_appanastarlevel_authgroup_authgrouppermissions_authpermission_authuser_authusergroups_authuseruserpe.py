# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-09-27 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppAnaStarlevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_all', models.CharField(max_length=15)),
                ('commodity_one', models.CharField(max_length=15)),
                ('commodity_two', models.CharField(max_length=15)),
                ('commodity_three', models.CharField(max_length=15)),
                ('commodity_four', models.CharField(max_length=15)),
                ('commodity_five', models.CharField(max_length=15)),
                ('comm_pro_one', models.CharField(max_length=10)),
                ('comm_pro_two', models.CharField(max_length=10)),
                ('comm_pro_three', models.CharField(max_length=10)),
                ('comm_pro_four', models.CharField(max_length=10)),
                ('comm_pro_five', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'app_ana_starlevel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BusProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('eva_num', models.CharField(blank=True, max_length=255, null=True)),
                ('score', models.CharField(blank=True, max_length=255, null=True)),
                ('percent_rate', models.CharField(blank=True, max_length=255, null=True)),
                ('pro_url', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('keep_time', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_size', models.CharField(blank=True, max_length=255, null=True)),
                ('seller_key', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_rating', models.CharField(blank=True, max_length=255, null=True)),
                ('con_home_url', models.CharField(blank=True, max_length=255, null=True)),
                ('create_by', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('is_del', models.CharField(blank=True, max_length=1, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'bus_prod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BusStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_by', models.CharField(blank=True, max_length=50, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('is_del', models.CharField(blank=True, max_length=1, null=True)),
                ('json', models.TextField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'bus_star',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysArea',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('value', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('sort', models.IntegerField(blank=True, null=True)),
                ('subsite_code', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'sys_area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysCity',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('pid', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('areaid', models.CharField(blank=True, max_length=100, null=True)),
                ('is_open', models.CharField(blank=True, max_length=10, null=True)),
                ('create_by', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('is_del', models.CharField(blank=True, max_length=255, null=True)),
                ('is_vr_pc_top', models.CharField(blank=True, max_length=1, null=True)),
                ('is_vr_are_top', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'sys_city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysDict',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('value', models.TextField()),
                ('label', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('sort', models.CharField(max_length=255)),
                ('create_by', models.CharField(max_length=255)),
                ('create_date', models.DateField()),
                ('is_del', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('is_enable', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sys_dict',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_type', models.CharField(blank=True, max_length=255, null=True)),
                ('file_size', models.CharField(blank=True, max_length=255, null=True)),
                ('file_suffix', models.CharField(blank=True, max_length=255, null=True)),
                ('file_path', models.CharField(blank=True, max_length=255, null=True)),
                ('create_by', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('is_del', models.CharField(blank=True, max_length=255, null=True)),
                ('old_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gt_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sys_file',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysMenu',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('menuto', models.CharField(blank=True, max_length=60, null=True)),
                ('create_by', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('is_del', models.CharField(blank=True, max_length=255, null=True)),
                ('pid', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('sort', models.IntegerField(blank=True, null=True)),
                ('href', models.CharField(blank=True, max_length=255, null=True)),
                ('permission', models.TextField(blank=True, null=True)),
                ('is_show', models.CharField(blank=True, max_length=255, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('miaoshu', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
                ('open_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sys_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysMenusTo',
            fields=[
                ('id', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('create_by', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('is_del', models.CharField(blank=True, max_length=1, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('sort', models.IntegerField(blank=True, null=True)),
                ('is_show', models.CharField(blank=True, max_length=1, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('is_platform', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'sys_menus_to',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysMoblieCode',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('moblie', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('create_by', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('is_del', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sys_moblie_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysRole',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('role_name', models.CharField(blank=True, max_length=100, null=True)),
                ('role_ename', models.CharField(max_length=255)),
                ('is_enable', models.CharField(max_length=100)),
                ('create_by', models.CharField(max_length=255)),
                ('create_date', models.DateField()),
                ('is_del', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sys_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysRoleMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(max_length=100)),
                ('menu_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sys_role_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SystemProvinceCity',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('parentid', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('areaid', models.CharField(blank=True, max_length=100, null=True)),
                ('isopen', models.CharField(blank=True, max_length=1, null=True)),
                ('create_by', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('is_del', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'system_province_city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('create_by', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('login_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_del', models.CharField(blank=True, max_length=255, null=True)),
                ('is_enable', models.CharField(blank=True, max_length=32, null=True)),
                ('customer_type', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('service_qq', models.CharField(blank=True, max_length=20, null=True)),
                ('service_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('pass_str', models.CharField(blank=True, max_length=255, null=True)),
                ('linkman', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('balance', models.FloatField(blank=True, null=True)),
                ('channel_open_id', models.CharField(blank=True, max_length=255, null=True)),
                ('channel_duty_id', models.CharField(blank=True, max_length=255, null=True)),
                ('service_id', models.CharField(blank=True, max_length=255, null=True)),
                ('rebate_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('channel_level', models.IntegerField(blank=True, null=True)),
                ('weichat_no', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('channel_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sys_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysUserAddress',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('create_by', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('is_del', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sys_user_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysUserLog',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('update_user', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('create_by', models.CharField(blank=True, max_length=255, null=True)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
                ('is_del', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sys_user_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysUserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('role_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sys_user_role',
                'managed': False,
            },
        ),
    ]