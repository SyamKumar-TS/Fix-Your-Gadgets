# Generated by Django 4.1.6 on 2023-02-17 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='admin_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]