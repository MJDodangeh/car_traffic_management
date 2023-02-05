# Generated by Django 4.1.5 on 2023-02-01 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.IntegerField(default=0)),
                ('latitude', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=32, null=True)),
                ('from_node', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fromnode', to='maps.node')),
                ('to_node', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tonode', to='maps.node')),
            ],
        ),
    ]
