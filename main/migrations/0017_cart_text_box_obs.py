# Generated by Django 4.2 on 2023-05-29 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='text_box_obs',
            field=models.TextField(blank=True),
        ),
    ]
