# Generated by Django 3.1 on 2020-08-28 03:07

import apps.hueca.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classification', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hueca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classification.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classification.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('hueca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hueca.hueca')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.hueca.models.get_upload_to)),
                ('hueca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hueca.hueca')),
            ],
        ),
    ]
