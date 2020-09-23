# Generated by Django 2.2.16 on 2020-09-23 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200923_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.User'),
        ),
        migrations.AddField(
            model_name='reply',
            name='upload_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
