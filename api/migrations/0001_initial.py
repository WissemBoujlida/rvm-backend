# Generated by Django 4.2 on 2023-05-10 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecyclableItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container', models.CharField(choices=[('BOTTLE', 'Bottle'), ('CAN', 'Can')], max_length=30)),
                ('material', models.CharField(choices=[('PLASTIC', 'Plastic'), ('ALUMINIUM', 'Aluminium')], max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('volume', models.FloatField()),
                ('beverageType', models.CharField(choices=[('WATER', 'Water'), ('SODA', 'Soda')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RVM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(0, 'Faulty'), (1, 'Working'), (2, 'Maintenance')])),
            ],
        ),
        migrations.CreateModel(
            name='RecyclingTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionDate', models.DateTimeField()),
                ('totalRecompense', models.FloatField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rvm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rvm')),
            ],
        ),
        migrations.CreateModel(
            name='RecyclingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('recyclableItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.recyclableitem')),
                ('recyclingTransaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.recyclingtransaction')),
            ],
            options={
                'unique_together': {('recyclingTransaction', 'recyclableItem')},
            },
        ),
    ]
