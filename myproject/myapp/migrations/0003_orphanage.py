# Generated by Django 5.1.4 on 2024-12-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_fooditem_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orphanage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
