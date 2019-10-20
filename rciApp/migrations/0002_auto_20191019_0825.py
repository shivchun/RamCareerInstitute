# Generated by Django 2.2.6 on 2019-10-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rciApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_class', models.CharField(choices=[('12th', '12th'), ('11th', '11th'), ('Target', 'Target'), ('10th', '10th'), ('9th', '9th'), ('8th', '8th'), ('7th', '7th'), ('6th', '6th')], default='12th', max_length=10)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='studentenquiry',
            name='presentClass',
            field=models.IntegerField(choices=[(6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=6),
        ),
        migrations.AlterField(
            model_name='studentenquiry',
            name='stream',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Medical', 'Medical'), ('6th,7th,8th,9th,10th', '6th,7th,8th,9th,10th')], default='Engineering', max_length=20),
        ),
    ]