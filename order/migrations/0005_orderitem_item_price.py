# Generated by Django 3.0.3 on 2020-09-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200907_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='item_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
