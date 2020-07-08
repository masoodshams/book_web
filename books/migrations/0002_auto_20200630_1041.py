# Generated by Django 3.0.7 on 2020-06-30 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='character',
            field=models.ManyToManyField(null=True, to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='parent_book',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='place_in_serie',
            field=models.DecimalField(decimal_places=0, default=None, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='series_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Series'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series_rel_type',
            field=models.CharField(choices=[('Main', 'Main'), ('Spin Off', 'Spin Off'), ('OVA', 'OVA')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='parent_series',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Series'),
        ),
        migrations.AlterField(
            model_name='series',
            name='place',
            field=models.DecimalField(decimal_places=0, default=None, max_digits=3, null=True),
        ),
    ]
