# Generated by Django 4.1.6 on 2023-03-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_admin', '0002_alter_article_recomendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='recomendation',
            field=models.IntegerField(default=0),
        ),
    ]