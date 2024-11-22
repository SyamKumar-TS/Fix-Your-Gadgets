# Generated by Django 4.1.6 on 2023-02-04 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0004_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_gender', models.CharField(max_length=50)),
                ('user_contact', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_photo', models.FileField(upload_to='UserDocs/')),
                ('user_proof', models.FileField(upload_to='UserDocs/')),
                ('user_password', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=100)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
    ]