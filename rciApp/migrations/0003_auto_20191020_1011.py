# Generated by Django 2.2.6 on 2019-10-20 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rciApp', '0002_auto_20191019_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_batch',
            name='batch_class',
            field=models.CharField(choices=[('12th', '12th'), ('11th', '11th'), ('Target', 'Target'), ('10th', '10th'), ('9th', '9th'), ('8th', '8th'), ('7th', '7th'), ('6th', '6th')], default='12th', max_length=10, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='new_batch',
            name='start_date',
            field=models.DateField(verbose_name='Starting Date of Batch'),
        ),
        migrations.AlterField(
            model_name='studentenquiry',
            name='mobileNo',
            field=models.IntegerField(verbose_name='mobile No'),
        ),
        migrations.AlterField(
            model_name='studentenquiry',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='studentenquiry',
            name='presentClass',
            field=models.IntegerField(choices=[(6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=6, verbose_name='Present Class'),
        ),
        migrations.AlterField(
            model_name='studentenquiry',
            name='stream',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Medical', 'Medical'), ('6th,7th,8th,9th,10th', '6th,7th,8th,9th,10th')], default='Engineering', max_length=20, verbose_name='Stream'),
        ),
    ]
