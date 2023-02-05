# Generated by Django 4.1.5 on 2023-02-01 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('color', models.CharField(max_length=32)),
                ('loc_nextnode_distance', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('sedan', 'sedan'), ('lorry', 'lorry')], default='sedan', max_length=5)),
                ('loc_edge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.edge')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('national_code', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sedan',
            fields=[
                ('car_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cars.car')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.owner')),
            ],
            bases=('cars.car',),
        ),
        migrations.CreateModel(
            name='Lorry',
            fields=[
                ('car_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cars.car')),
                ('load_weight', models.IntegerField(default=0)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.owner')),
            ],
            bases=('cars.car',),
        ),
    ]
