# Generated by Django 3.2 on 2022-05-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcebank', '0017_testsave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsave',
            name='add_file',
            field=models.FileField(blank=True, null=True, upload_to='answer_attachment/'),
        ),
    ]
