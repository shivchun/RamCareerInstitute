# Generated by Django 2.2.6 on 2019-10-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0006_auto_20191020_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam_registration_class_10',
            name='date_of_exam',
        ),
        migrations.RemoveField(
            model_name='exam_registration_class_11',
            name='date_of_exam',
        ),
        migrations.RemoveField(
            model_name='exam_registration_class_12',
            name='date_of_exam',
        ),
        migrations.RemoveField(
            model_name='exam_registration_class_6',
            name='date_of_exam',
        ),
        migrations.RemoveField(
            model_name='exam_registration_class_7',
            name='date_of_exam',
        ),
        migrations.RemoveField(
            model_name='exam_registration_class_8',
            name='date_of_exam',
        ),
        migrations.RemoveField(
            model_name='exam_registration_class_9',
            name='date_of_exam',
        ),
        migrations.RemoveField(
            model_name='exam_registration_target',
            name='date_of_exam',
        ),
        migrations.AddField(
            model_name='exam_registration_class_10',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='exam_registration_class_11',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='exam_registration_class_12',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='exam_registration_class_6',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='exam_registration_class_7',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='exam_registration_class_8',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='exam_registration_class_9',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='exam_registration_target',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
    ]
