# Generated by Django 3.1.2 on 2020-10-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
