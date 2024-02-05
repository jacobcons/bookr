# Generated by Django 5.0.1 on 2024-02-05 15:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contributor",
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
                ("first_names", models.CharField(max_length=50)),
                ("last_names", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name="publisher",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="publisher",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="publisher",
            name="website",
            field=models.URLField(),
        ),
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=70)),
                ("publication_date", models.DateField()),
                ("isbn", models.CharField(max_length=20)),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="books",
                        to="reviews.publisher",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookContributor",
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
                    "role",
                    models.CharField(
                        choices=[
                            ("AUTHOR", "Author"),
                            ("CO_AUTHOR", "Co-Author"),
                            ("EDITOR", "Editor"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="reviews.book"
                    ),
                ),
                (
                    "contributor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reviews.contributor",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="contributors",
            field=models.ManyToManyField(
                related_name="books",
                through="reviews.BookContributor",
                to="reviews.contributor",
            ),
        ),
        migrations.CreateModel(
            name="Review",
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
                ("text", models.TextField()),
                ("rating", models.IntegerField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "date_edited",
                    models.DateTimeField(
                        help_text="The last date and time the review was edited",
                        null=True,
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="reviews.book",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]