# Generated by Django 4.2.3 on 2023-07-22 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "quotation",
            "0003_shippingaddress_order_transaction_id_delete_shipping_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="data_ordered",
            new_name="date_ordered",
        ),
        migrations.RenameField(
            model_name="orderitem",
            old_name="data_added",
            new_name="date_added",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="user",
        ),
    ]
