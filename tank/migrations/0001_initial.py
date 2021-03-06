# Generated by Django 4.0.4 on 2022-04-22 17:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Jméno/název várobce:')),
            ],
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Název motoru:')),
                ('cylinders', models.IntegerField(validators=[django.core.validators.MaxValueValidator(14)])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Jméno státu')),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Název tanku:')),
                ('description', models.TextField(verbose_name='Popis tanku:')),
                ('type', models.CharField(choices=[('light', 'Lehký tank'), ('medium', 'Střední tank'), ('heavy', 'Těžký tank'), ('td', 'stíhač tanků'), ('arty', 'Dělostřelectvo')], help_text='Vyberte typ vozidla', max_length=50, verbose_name='Typ vozidla:')),
                ('pressence', models.CharField(choices=[('1.', 'V 1. světové válce'), ('2.', 'V 2. světové válce'), ('3.', 'V jiné'), ('0.', 'V žádné')], help_text='Vyberte období, ve kterém se vozidlo vyskytovalo', max_length=50, verbose_name='Výskyt:')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tank.nationality', verbose_name='Stát:')),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range', models.IntegerField(help_text='Vepište maximální dojezd vozidla (V kilometrech)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Maximální dojezd:')),
                ('maxspeed', models.IntegerField(help_text='Vepište maximální rychlost vozidla (V metrech za hodinu)', validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(150)], verbose_name='Maximální rychlost')),
                ('motor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tank.motor', verbose_name='Motor:')),
            ],
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], help_text='Vyberte počet členů posádky', max_length=1, verbose_name='Členové posádky:')),
                ('length', models.DecimalField(decimal_places=2, help_text='Vepište délku vozidla (v metrech)', max_digits=4, verbose_name='Délka vozidla:')),
                ('width', models.DecimalField(decimal_places=2, help_text='Vepište šířku vozidla (v metrech)', max_digits=3, verbose_name='Šířka vozidla:')),
                ('height', models.DecimalField(decimal_places=2, help_text='Vepište výšku vozidla (v metrech)', max_digits=3, verbose_name='Výška vozidla:')),
                ('mass', models.IntegerField(help_text='Vepište váhu vozidla (v tunách)', validators=[django.core.validators.MaxValueValidator(250)], verbose_name='Váha vozidla:')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tank.maker', verbose_name='Výrobce:')),
            ],
        ),
    ]
