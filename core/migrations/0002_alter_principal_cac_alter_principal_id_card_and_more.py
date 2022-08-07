# Generated by Django 4.1 on 2022-08-06 17:10

import core.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='CAC',
            field=models.FileField(default='default_id.png', upload_to=core.models.get_credentials_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'pdf', 'png'])]),
        ),
        migrations.AlterField(
            model_name='principal',
            name='id_card',
            field=models.FileField(default='default_id.png', upload_to=core.models.get_credentials_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'pdf', 'png'])]),
        ),
        migrations.AlterField(
            model_name='principal',
            name='letter',
            field=models.FileField(default='default_id.png', upload_to=core.models.get_credentials_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'pdf', 'png'])]),
        ),
    ]