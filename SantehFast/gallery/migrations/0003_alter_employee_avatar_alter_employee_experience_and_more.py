# Generated by Django 5.0.4 on 2024-04-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_employee_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='experience',
            field=models.IntegerField(blank=True, null=True, verbose_name='Опыт работы'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='patronymic',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='images/work'),
        ),
    ]
