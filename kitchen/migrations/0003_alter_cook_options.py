# Generated by Django 4.2.7 on 2023-11-22 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_alter_cook_years_of_experience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cook',
            options={'verbose_name': 'cook', 'verbose_name_plural': 'cooks'},
        ),
    ]