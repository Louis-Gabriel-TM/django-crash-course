# Generated by Django 3.0.8 on 2020-08-06 13:20

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='country_of_origin',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country of Origin'),
        ),
        migrations.AlterField(
            model_name='cheese',
            name='firmness',
            field=models.CharField(choices=[('non spécifié', 'Non spécifié'), ('pâte molle', 'Pâte molle'), ('pâte demi-molle', 'Pâte demi-molle'), ('pâte demi-dure', 'Pâte demi-dure'), ('pâte dure', 'Pâte dure')], default='non spécifié', max_length=20, verbose_name='fermeté'),
        ),
    ]