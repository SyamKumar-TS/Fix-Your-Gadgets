# Generated by Django 4.1.6 on 2023-02-25 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_admin_admin_name'),
        ('Admin', '0005_technician'),
        ('User', '0003_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='technician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.technician'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.user'),
        ),
    ]