# Generated by Django 2.2.4 on 2019-08-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190827_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.FileField(default=False, upload_to='images/'),
        ),
    ]
