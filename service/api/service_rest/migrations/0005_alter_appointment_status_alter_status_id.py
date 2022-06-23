# Generated by Django 4.0.3 on 2022-06-22 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0004_alter_status_options_alter_status_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[(0, 'scheduled'), (1, 'finished'), (2, 'canceled')], default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]