# Generated by Django 5.0.3 on 2024-03-28 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GroupeTontine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupetontine',
            old_name='montant',
            new_name='montantCotisation',
        ),
    ]
