# Generated by Django 3.2.9 on 2021-12-01 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0004_alter_record_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='customer',
            field=models.ForeignKey(blank=True, default='None', on_delete=django.db.models.deletion.CASCADE, to='beauty.person'),
        ),
    ]