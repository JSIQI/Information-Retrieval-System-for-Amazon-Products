# Generated by Django 2.0.5 on 2018-05-31 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0002_auto_20180531_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='P_id',
            field=models.IntegerField(),
        ),
    ]
