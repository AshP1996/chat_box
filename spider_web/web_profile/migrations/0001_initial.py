# Generated by Django 5.0.3 on 2024-03-22 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('description', models.TextField(blank=True, null=True)),
                ('links', models.URLField(blank=True)),
                ('id_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='web_user.customuser')),
            ],
        ),
    ]
