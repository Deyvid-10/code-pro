# Generated by Django 4.2.7 on 2023-11-20 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
