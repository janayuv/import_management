# Generated by Django 5.1.2 on 2024-11-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmaster',
            name='part_description',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
