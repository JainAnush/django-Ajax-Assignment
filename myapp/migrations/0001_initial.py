# Generated by Django 4.0.4 on 2022-06-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
                ('correctans', models.IntegerField()),
            ],
        ),
    ]
