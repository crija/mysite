# Generated by Django 4.1.7 on 2023-05-24 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_people_alter_question_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='data_criaçao',
            new_name='data_criacao',
        ),
        migrations.AlterField(
            model_name='people',
            name='idade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='people',
            name='peso',
            field=models.IntegerField(),
        ),
    ]
