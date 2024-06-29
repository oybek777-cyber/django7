# Generated by Django 5.0.4 on 2024-04-23 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allworld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abount_user', models.TextField()),
                ('image', models.ImageField(upload_to='user_image')),
                ('awarsd', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='repsentred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('name', models.CharField(max_length=40)),
                ('p_numner', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='categroy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nema', models.CharField(max_length=40)),
                ('allworld', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.allworld')),
            ],
        ),
        migrations.CreateModel(
            name='exbiations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('describtions', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='rapsentred_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.repsentred'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=40)),
                ('l_name', models.CharField(max_length=40)),
                ('p_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('linkdir', models.URLField()),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('image', models.ImageField(upload_to='image')),
                ('all_world', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.allworld')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user'),
        ),
    ]
