# Generated by Django 3.2 on 2022-05-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcebank', '0019_remove_answers_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='answer_attachment'),
        ),
    ]
