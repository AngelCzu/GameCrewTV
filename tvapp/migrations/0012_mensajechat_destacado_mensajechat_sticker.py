# Generated by Django 4.2.6 on 2023-11-27 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvapp', '0011_sala_mensajechat'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajechat',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mensajechat',
            name='sticker',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]