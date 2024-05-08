# Generated by Django 5.0.4 on 2024-05-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('county_name', models.CharField(max_length=100)),
                ('county_no', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('project_type_name', models.CharField(default='Commercial', max_length=100)),
                ('project_type_no', models.IntegerField(default=1, primary_key=True, serialize=False)),
            ],
        ),
    ]
