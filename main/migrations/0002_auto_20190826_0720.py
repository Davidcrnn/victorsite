# Generated by Django 2.2.4 on 2019-08-26 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='serie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Serie'),
        ),
    ]