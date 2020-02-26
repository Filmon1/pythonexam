# Generated by Django 2.2 on 2020-02-24 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('Username', models.CharField(max_length=255)),
                ('passsword', models.CharField(max_length=255)),
                ('confirmPW', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('travel_start_date', models.DateField()),
                ('travel_End_Date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joinedTraveler', models.ManyToManyField(related_name='trip_joined', to='pythonbeltexamApp.User')),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='pythonbeltexamApp.User')),
            ],
        ),
    ]