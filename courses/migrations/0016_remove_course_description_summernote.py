# Generated by Django 4.1.3 on 2024-09-21 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_course_description_summernote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description_summernote',
        ),
    ]
