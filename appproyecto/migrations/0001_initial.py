# Generated by Django 4.1.3 on 2022-12-12 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=50)),
                ('año_nacimiento', models.IntegerField()),
                ('dni', models.IntegerField()),
            ],
        ),
    ]
