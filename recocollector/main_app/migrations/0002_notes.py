# Generated by Django 3.0.3 on 2020-04-09 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('opinion', models.TextField(max_length=500)),
                ('reco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Reco')),
            ],
        ),
    ]
