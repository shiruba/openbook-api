# Generated by Django 2.1.3 on 2018-11-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emoji',
            name='name',
        ),
        migrations.RemoveField(
            model_name='emoji',
            name='shortcut',
        ),
        migrations.AddField(
            model_name='emoji',
            name='keyword',
            field=models.CharField(default='wot', max_length=16, verbose_name='keyword'),
            preserve_default=False,
        ),
    ]
