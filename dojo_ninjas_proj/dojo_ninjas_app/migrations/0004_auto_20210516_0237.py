# Generated by Django 2.2 on 2021-05-16 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0003_auto_20210516_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninjas',
            old_name='dojo_id',
            new_name='dojos',
        ),
    ]
