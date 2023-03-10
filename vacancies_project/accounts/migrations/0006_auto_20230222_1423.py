# Generated by Django 3.2.16 on 2023-02-22 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_auto_20230221_2205"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="applicant",
            options={"verbose_name": "Соискатель", "verbose_name_plural": "Соискатели"},
        ),
        migrations.AlterModelOptions(
            name="employer",
            options={
                "verbose_name": "Работодатель",
                "verbose_name_plural": "Работодатели",
            },
        ),
        migrations.AlterModelOptions(
            name="experience",
            options={
                "ordering": ("-pk",),
                "verbose_name": "Опыт",
                "verbose_name_plural": "Опыт",
            },
        ),
        migrations.RemoveField(
            model_name="applicant",
            name="is_employer",
        ),
        migrations.RemoveField(
            model_name="employer",
            name="is_employer",
        ),
    ]
