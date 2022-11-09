# Generated by Django 4.1.3 on 2022-11-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_review', '0005_profile_experiment_two_retake_count_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hasConsent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='survey_one_isComplete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='survey_two_isComplete',
            field=models.BooleanField(default=False),
        ),
    ]
