# Generated by Django 2.2b1 on 2019-03-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0020_auto_20190309_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='height',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='width',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]