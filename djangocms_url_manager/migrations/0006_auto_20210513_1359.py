# Generated by Django 2.2.20 on 2021-05-13 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_url_manager', '0005_auto_20200923_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='djangocms_url_manager_url_content_type', to='contenttypes.ContentType'),
        ),
    ]
