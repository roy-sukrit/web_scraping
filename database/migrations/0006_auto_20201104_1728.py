# Generated by Django 3.1.2 on 2020-11-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20201104_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='myData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LogoLinks', models.CharField(max_length=122)),
                ('LogoName', models.CharField(max_length=122)),
            ],
        ),
        migrations.DeleteModel(
            name='myDataBase',
        ),
    ]
