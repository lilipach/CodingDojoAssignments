# Generated by Django 2.2 on 2021-05-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='this is a dojo'),
        ),
        migrations.AlterField(
            model_name='dojo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ninjas',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]