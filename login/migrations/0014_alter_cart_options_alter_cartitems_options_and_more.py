# Generated by Django 4.2.1 on 2023-06-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0013_alter_cart_options_alter_cartitems_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cart", options={"verbose_name_plural": "Carts"},
        ),
        migrations.AlterModelOptions(
            name="cartitems", options={"verbose_name_plural": "Cart Items"},
        ),
        migrations.AlterModelOptions(
            name="category", options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="colorvariant", options={"verbose_name_plural": "Color Variants"},
        ),
        migrations.AlterModelOptions(
            name="product", options={"verbose_name_plural": "Products"},
        ),
        migrations.AlterModelOptions(
            name="sizevariant", options={"verbose_name_plural": "Size Variants"},
        ),
        migrations.AlterField(
            model_name="category",
            name="category_name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(upload_to="products"),
        ),
    ]
