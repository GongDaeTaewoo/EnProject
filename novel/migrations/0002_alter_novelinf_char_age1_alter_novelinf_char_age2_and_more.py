# Generated by Django 4.2.3 on 2023-07-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelinf',
            name='char_age1',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='novelinf',
            name='char_age2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='novelinf',
            name='char_name1',
            field=models.CharField(blank=True, default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='novelinf',
            name='char_name2',
            field=models.CharField(blank=True, default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='novelinf',
            name='char_per1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='novelinf',
            name='char_per2',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]