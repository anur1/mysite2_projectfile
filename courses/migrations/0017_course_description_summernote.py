# Generated by Django 4.1.3 on 2024-09-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_remove_course_description_summernote'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description_summernote',
            field=models.CharField(default='asas', max_length=50000),
            preserve_default=False,
        ),
    ]
