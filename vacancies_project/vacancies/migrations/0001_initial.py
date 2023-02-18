# Generated by Django 3.2.16 on 2023-02-18 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('salary', models.PositiveIntegerField(verbose_name='Зарплата')),
                ('description', models.CharField(max_length=3000, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='vacancy', verbose_name='Картинка')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='accounts.employer')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='accounts.applicant')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='vacancies.vacancy')),
            ],
        ),
    ]
