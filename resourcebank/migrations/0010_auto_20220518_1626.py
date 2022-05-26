# Generated by Django 3.2 on 2022-05-18 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resourcebank', '0009_auto_20220518_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='resourcebank.answerrating'),
        ),
        migrations.AddField(
            model_name='questions',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='resourcebank.questionrating'),
        ),
    ]
