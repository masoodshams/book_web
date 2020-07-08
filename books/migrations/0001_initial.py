# Generated by Django 3.0.7 on 2020-06-28 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('place', models.DecimalField(decimal_places=0, max_digits=3, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_series', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Series')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('place_in_book', models.DecimalField(decimal_places=0, max_digits=3)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Series')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('isbn', models.DecimalField(decimal_places=0, max_digits=13, unique=True)),
                ('language', models.CharField(max_length=50)),
                ('edition', models.PositiveSmallIntegerField()),
                ('series_rel_type', models.CharField(choices=[('Main', 'Main'), ('Spin Off', 'Spin Off'), ('OVA', 'OVA')], max_length=100, null=True)),
                ('place_in_serie', models.DecimalField(decimal_places=0, max_digits=3, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('series_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Series')),
            ],
        ),
    ]