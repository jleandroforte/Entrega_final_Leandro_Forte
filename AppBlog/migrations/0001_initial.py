# Generated by Django 4.2 on 2023-05-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=999)),
                ('subtitulo', models.CharField(max_length=999)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('autor', models.CharField(max_length=255)),
            ],
        ),
    ]
