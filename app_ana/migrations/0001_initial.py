# Generated by Django 2.1.1 on 2019-09-27 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StarLevel',
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
        ),
    ]