# Generated by Django 5.1.1 on 2024-09-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('file_name', models.CharField(max_length=255)),
                ('qr_image', models.ImageField(upload_to='qr_codes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]