# Generated by Django 2.2.7 on 2019-11-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_atracao_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='observacoes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
