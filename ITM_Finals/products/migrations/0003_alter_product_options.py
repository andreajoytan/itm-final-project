# Generated by Django 4.2.3 on 2023-07-21 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_options_product_modified_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ("-publish_date",)},
        ),
    ]
