# Generated by Django 4.2.2 on 2023-06-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djuser',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
