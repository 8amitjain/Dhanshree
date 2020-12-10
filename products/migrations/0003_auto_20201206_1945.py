# Generated by Django 3.1.3 on 2020-12-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productcontact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcontact',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AlterField(
            model_name='productcontact',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]