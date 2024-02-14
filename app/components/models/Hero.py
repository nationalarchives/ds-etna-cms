from app.images.blocks import APIImageChooserBlock
from wagtail.blocks import CharBlock, RichTextBlock, StructBlock


class Hero(StructBlock):
    heading = CharBlock(
        max_length=100,
        label="Heading",
        required=False,
    )

    body = RichTextBlock(
        features=["bold", "italic", "link"],
        label="Body",
        required=False,
    )

    image = APIImageChooserBlock(
        {
            "large": "fill-1200x480|format-jpeg|jpegquality-60",
            "large_webp": "fill-1200x480|format-webp|webpquality-80",
            "small": "fill-600x400|format-jpeg|jpegquality-60",
            "small_webp": "fill-600x400|format-webp|webpquality-80",
        },
        required=True,
    )
