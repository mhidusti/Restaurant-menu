# Generated by Django 5.1.7 on 2025-06-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=15, verbose_name='شماره تلفن')),
                ('date', models.DateField(verbose_name='روز')),
                ('time', models.TimeField(verbose_name='زمان')),
                ('people', models.PositiveIntegerField(verbose_name='تعداد')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
            ],
            options={
                'verbose_name': 'رزرو میز',
                'ordering': ['-created_date'],
            },
        ),
    ]
