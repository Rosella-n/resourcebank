# Generated by Django 3.2 on 2022-11-13 09:54

from django.db import migrations, models
import validators


class Migration(migrations.Migration):

    dependencies = [
        ('resourcebank', '0024_questions_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='add_file',
            field=models.FileField(blank=True, null=True, upload_to='material_upload/', validators=[validators.pdfvalidator]),
        ),
    ]
