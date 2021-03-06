# Generated by Django 2.0.5 on 2018-05-31 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='star',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
