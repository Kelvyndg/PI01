# Generated by Django 2.2.24 on 2021-11-15 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211115_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='responsavel',
            new_name='aluno',
        ),
    ]
