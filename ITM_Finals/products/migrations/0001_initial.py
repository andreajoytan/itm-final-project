# Generated by Django 4.2.3 on 2023-07-19 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(
                        help_text="Enter product category.", max_length=250
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
                "ordering": ("category_name",),
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(help_text="Enter product name.", max_length=250),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Enter product description.", null=True
                    ),
                ),
                ("price", models.FloatField(help_text="Enter product price.")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Upload product image.",
                        null=True,
                        upload_to="product_images",
                    ),
                ),
                ("available", models.BooleanField(default=True)),
                ("publish_date", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.category",
                    ),
                ),
            ],
        ),
    ]
