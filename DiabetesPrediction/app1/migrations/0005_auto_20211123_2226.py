# Generated by Django 2.2.5 on 2021-11-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_userdatas_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdatas',
            name='result',
        ),
        migrations.AlterField(
            model_name='userdatas',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usernames',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
