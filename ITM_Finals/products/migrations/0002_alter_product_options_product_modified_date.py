# Generated by Django 4.2.3 on 2023-07-21 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ("-modified_date",)},
        ),
        migrations.AddField(
            model_name="product",
            name="modified_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]