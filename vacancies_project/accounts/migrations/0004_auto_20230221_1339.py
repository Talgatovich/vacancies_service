# Generated by Django 3.2.16 on 2023-02-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20230221_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='contacts',
        ),
        migrations.AddField(
            model_name='applicant',
            name='address',
            field=models.CharField(blank=True, max_length=300, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='city',
            field=models.CharField(default=1, max_length=50, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='tg_link',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ссылка на телеграм'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='vk_link',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ссылка в вк'),
        ),
        migrations.AddField(
            model_name='employer',
            name='address',
            field=models.CharField(blank=True, max_length=300, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='employer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='employer',
            name='tg_link',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ссылка на телеграм'),
        ),
        migrations.AddField(
            model_name='employer',
            name='vk_link',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ссылка в вк'),
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]
