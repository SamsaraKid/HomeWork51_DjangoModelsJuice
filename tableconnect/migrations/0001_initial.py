# Generated by Django 4.2.5 on 2023-09-17 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('volume', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pack', models.CharField(max_length=10)),
                ('recomend', models.BooleanField(null=True)),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableconnect.company')),
            ],
        ),
    ]
