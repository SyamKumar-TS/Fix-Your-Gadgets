# Generated by Django 4.1.6 on 2023-03-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_delete_ewastecollector'),
    ]

    operations = [
        migrations.CreateModel(
            name='EwasteCollector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EwasteCollector_name', models.CharField(max_length=50)),
                ('EwasteCollector_contact', models.CharField(max_length=50)),
                ('EwasteCollector_email', models.CharField(max_length=50)),
                ('EwasteCollector_photo', models.FileField(upload_to='CollectorDocs/')),
                ('EwasteCollector_proof', models.FileField(upload_to='CollectorDocs/')),
                ('EwasteCollector_password', models.CharField(max_length=50)),
                ('EwasteCollector_vehicleno', models.CharField(max_length=50)),
                ('EwasteCollector_vehiclemodel', models.CharField(max_length=50)),
                ('EwasteCollector_vehicleimg', models.FileField(upload_to='CollectorDocs/')),
            ],
        ),
    ]