# Generated by Django 4.1.7 on 2023-05-29 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_people_peso_people_sexo_pet_raca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('cor', models.CharField(max_length=20)),
                ('ano', models.CharField(max_length=4)),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.people')),
            ],
        ),
    ]
