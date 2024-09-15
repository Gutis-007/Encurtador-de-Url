# Generated by Django 5.1.1 on 2024-09-15 22:56

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url_original', models.URLField(max_length=500)),
                ('chave', models.CharField(blank=True, default=api.models.gerarchave, max_length=10, null=True, unique=True)),
            ],
        ),
    ]