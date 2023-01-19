# Generated by Django 4.1.2 on 2023-01-16 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/')),
                ('product', models.FileField(upload_to='media/')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]