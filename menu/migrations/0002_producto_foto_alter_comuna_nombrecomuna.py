# Generated by Django 4.2.2 on 2023-07-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='comuna',
            name='nombreComuna',
            field=models.CharField(max_length=200),
        ),
    ]
