# Generated by Django 4.0.4 on 2022-04-22 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0002_alter_characteristics_options_alter_maker_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristics',
            name='tank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tank.tank', verbose_name='Tank:'),
            preserve_default=False,
        ),
    ]
