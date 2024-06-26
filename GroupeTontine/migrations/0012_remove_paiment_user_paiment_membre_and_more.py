# Generated by Django 5.0.3 on 2024-05-03 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupeTontine', '0011_paiment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paiment',
            name='user',
        ),
        migrations.AddField(
            model_name='paiment',
            name='membre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GroupeTontine.membre'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membre',
            name='adress',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='paiment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
