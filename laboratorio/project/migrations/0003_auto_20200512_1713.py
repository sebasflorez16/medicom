# Generated by Django 3.0.3 on 2020-05-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200512_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenes',
            name='exam',
            field=models.CharField(max_length=100, verbose_name='Tipo de examen'),
        ),
        migrations.AlterField(
            model_name='examenes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='examenes', verbose_name='Orden'),
        ),
    ]
