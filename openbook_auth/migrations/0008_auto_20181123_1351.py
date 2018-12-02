# Generated by Django 2.1.3 on 2018-11-23 12:51

from django.db import migrations, models
import openbook_common.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_auth', '0007_auto_20181122_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=192, validators=[openbook_common.validators.name_characters_validator], verbose_name='name'),
        ),
    ]
