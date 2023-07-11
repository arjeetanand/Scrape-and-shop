# Generated by Django 4.2.1 on 2023-06-21 17:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0003_rename_email_contactus_emailcon_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("category_name", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("category_image", models.ImageField(upload_to="catgories")),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="ColorVariant",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("color_name", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=0)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("product_name", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("price", models.IntegerField()),
                ("product_desription", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="login.category",
                    ),
                ),
                (
                    "color_variant",
                    models.ManyToManyField(blank=True, to="login.colorvariant"),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="SizeVariant",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("size_name", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=0)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(upload_to="product")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_images",
                        to="login.product",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.AddField(
            model_name="product",
            name="size_variant",
            field=models.ManyToManyField(blank=True, to="login.sizevariant"),
        ),
    ]