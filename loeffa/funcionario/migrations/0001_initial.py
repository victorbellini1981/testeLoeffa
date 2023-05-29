# Generated by Django 4.2.1 on 2023-05-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('enome', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtato', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'funcionario',
            },
        ),
    ]
