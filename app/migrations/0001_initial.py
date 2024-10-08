# Generated by Django 3.2.5 on 2021-07-15 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('ISBN', models.IntegerField(max_length=13)),
                ('publication_year', models.IntegerField(max_length=4)),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=4, null=True)),
                ('borrowing_price_per_day', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('status', models.CharField(blank=True, choices=[('available', 'available'), ('borrowed', 'borrowed'), ('sold', 'sold')], max_length=50, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category')),
            ],
        ),
    ]
