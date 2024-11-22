# Generated by Django 4.1.6 on 2023-04-13 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=50)),
                ('product_image', models.FileField(upload_to='ProductDocs/')),
                ('Product_description', models.CharField(max_length=100)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.type')),
            ],
        ),
    ]