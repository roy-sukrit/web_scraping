# Generated by Django 3.1.2 on 2020-11-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20201104_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedb',
            name='data',
            field=models.CharField(max_length=122),
        ),
    ]
