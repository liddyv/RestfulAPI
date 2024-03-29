# Generated by Django 2.2.3 on 2019-07-26 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_auto_20190720_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('to-do', 'To Do'), ('in-progress', 'In Progress'), ('done', 'Done')], default='to-do', max_length=250),
        ),
    ]
