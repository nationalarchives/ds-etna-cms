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

    image = APIImageChooserBlock("fill-1200x800", required=True)
