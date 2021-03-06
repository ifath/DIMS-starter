# Generated by Django 3.0.8 on 2020-07-20 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0003_auto_20200720_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='active_status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Modified At'),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
