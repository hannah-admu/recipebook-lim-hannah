# Generated by Django 5.0.2 on 2024-03-05 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_alter_recipeingredient_recipe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='recipeingredient',
            unique_together=set(),
        ),
    ]
