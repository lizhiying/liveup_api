# Generated by Django 3.2 on 2022-02-27 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20220227_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='status',
            field=models.CharField(choices=[('Admitted', 'Admitted'), ('Discharged', 'Discharged'), ('Not seen', 'Not seen'), ('In progress', 'In progress')], default='Not seen', max_length=20),
        ),
    ]
