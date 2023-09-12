# Generated by Django 4.0.3 on 2022-04-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_destination_link_alter_destination_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.FileField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('link', models.URLField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
