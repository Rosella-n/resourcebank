# Generated by Django 3.2 on 2022-05-18 15:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resourcebank', '0008_answer_rating'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer_Rating',
            new_name='AnswerRating',
        ),
        migrations.RenameModel(
            old_name='Question_Rating',
            new_name='QuestionRating',
        ),
    ]
