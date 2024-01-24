from app.components.blocks import APIRichTextBlock
from wagtail.blocks import CharBlock, StructBlock


class Blockquote(StructBlock):
    quote = APIRichTextBlock(
        features=[
            "bold",
            "italic",
            "link",
            "ol",
            "ul",
        ]
    )

    author = CharBlock(
        max_length=100,
        label="Author",
        required=False,
    )
