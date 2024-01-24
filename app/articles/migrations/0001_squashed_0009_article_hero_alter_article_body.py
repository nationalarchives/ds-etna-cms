# Generated by Django 5.0.1 on 2024-01-24 16:04

import app.components.blocks
import app.images.blocks
import app.records.blocks
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("articles", "0001_initial"),
        ("articles", "0002_article_body"),
        ("articles", "0003_alter_article_body"),
        ("articles", "0004_alter_article_body"),
        ("articles", "0005_alter_article_body"),
        ("articles", "0006_alter_article_body"),
        ("articles", "0007_alter_article_body"),
        ("articles", "0008_alter_article_body"),
        ("articles", "0009_article_hero_alter_article_body"),
    ]

    initial = True

    dependencies = [
        ("core", "0003_delete_exploreindex"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticlesIndex",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basepage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.basepage",),
        ),
        migrations.CreateModel(
            name="ExploreIndex",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basepage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.basepage",),
        ),
        migrations.CreateModel(
            name="FocusedArticle",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basepage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.basepage",),
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "basepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basepage",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "content_section",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(
                                                max_length=100
                                            ),
                                        ),
                                        (
                                            "content",
                                            wagtail.blocks.StreamBlock(
                                                [
                                                    (
                                                        "blockquote",
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "quote",
                                                                    app.components.blocks.APIRichTextBlock(
                                                                        features=[
                                                                            "bold",
                                                                            "italic",
                                                                            "link",
                                                                            "ol",
                                                                            "ul",
                                                                        ]
                                                                    ),
                                                                ),
                                                                (
                                                                    "author",
                                                                    wagtail.blocks.CharBlock(
                                                                        label="Author",
                                                                        max_length=100,
                                                                        required=False,
                                                                    ),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    (
                                                        "hero",
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "heading",
                                                                    wagtail.blocks.CharBlock(
                                                                        label="Heading",
                                                                        max_length=100,
                                                                        required=False,
                                                                    ),
                                                                ),
                                                                (
                                                                    "body",
                                                                    wagtail.blocks.RichTextBlock(
                                                                        features=[
                                                                            "bold",
                                                                            "italic",
                                                                            "link",
                                                                        ],
                                                                        label="Body",
                                                                        required=False,
                                                                    ),
                                                                ),
                                                                (
                                                                    "image",
                                                                    app.images.blocks.APIImageChooserBlock(
                                                                        {
                                                                            "large": "fill-1200x400|format-jpeg|jpegquality-60",
                                                                            "large_webp": "fill-1200x400|format-webp|webpquality-80",
                                                                            "small": "fill-600x400|format-jpeg|jpegquality-60",
                                                                            "small_webp": "fill-600x400|format-webp|webpquality-80",
                                                                        },
                                                                        required=True,
                                                                    ),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    (
                                                        "paragraph",
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "text",
                                                                    app.components.blocks.APIRichTextBlock(
                                                                        features=[
                                                                            "bold",
                                                                            "italic",
                                                                            "link",
                                                                            "ol",
                                                                            "ul",
                                                                        ]
                                                                    ),
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                    (
                                                        "picture",
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "image",
                                                                    app.images.blocks.APIImageChooserBlock(
                                                                        {
                                                                            "jpg": "max-1200x1200|format-jpeg|jpegquality-80",
                                                                            "webp": "max-1200x1200|format-webp|webpquality-80",
                                                                        },
                                                                        required=False,
                                                                    ),
                                                                ),
                                                                (
                                                                    "alt_text",
                                                                    wagtail.blocks.CharBlock(
                                                                        help_text='Alternative (alt) text describes images when they fail to load, and is read aloud by assistive technologies. Use a maximum of 100 characters to describe your image. Decorative images do not require alt text. <a href="https://html.spec.whatwg.org/multipage/images.html#alt" target="_blank">Check the guidance for tips on writing alt text</a>.',
                                                                        label="Image alternative text",
                                                                        max_length=100,
                                                                        required=False,
                                                                    ),
                                                                ),
                                                                (
                                                                    "caption",
                                                                    wagtail.blocks.RichTextBlock(
                                                                        features=[
                                                                            "bold",
                                                                            "italic",
                                                                            "link",
                                                                        ],
                                                                        help_text="An optional caption for non-decorative images, which will be displayed directly below the image. This could be used for image sources or for other useful metadata.",
                                                                        label="Caption (optional)",
                                                                        required=False,
                                                                    ),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    (
                                                        "featured_records",
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "items",
                                                                    wagtail.blocks.ListBlock(
                                                                        app.records.blocks.RecordLinkBlock
                                                                    ),
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                ],
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        use_json_field=True,
                    ),
                ),
                (
                    "hero",
                    wagtail.fields.StreamField(
                        [
                            (
                                "hero2",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(
                                                label="Heading",
                                                max_length=100,
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "body",
                                            wagtail.blocks.RichTextBlock(
                                                features=[
                                                    "bold",
                                                    "italic",
                                                    "link",
                                                ],
                                                label="Body",
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "image",
                                            app.images.blocks.APIImageChooserBlock(
                                                {
                                                    "large": "fill-1200x400|format-jpeg|jpegquality-60",
                                                    "large_webp": "fill-1200x400|format-webp|webpquality-80",
                                                    "small": "fill-600x400|format-jpeg|jpegquality-60",
                                                    "small_webp": "fill-600x400|format-webp|webpquality-80",
                                                },
                                                required=True,
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        use_json_field=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.basepage",),
        ),
    ]
