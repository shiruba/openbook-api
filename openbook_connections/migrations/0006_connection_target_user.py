# Generated by Django 2.1.3 on 2018-12-13 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openbook_connections', '0005_remove_connection_circle'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='target_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='targeted_connections', to=settings.AUTH_USER_MODEL),
        ),
    ]
