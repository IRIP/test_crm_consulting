# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 15:18


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20181002_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='businessOwner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_business_owner', to='people.Consultant', verbose_name='Business owner'),
        ),
    ]
