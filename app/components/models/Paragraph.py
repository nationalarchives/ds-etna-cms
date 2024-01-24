from app.components.blocks import APIRichTextBlock
from wagtail.blocks import StructBlock


class Paragraph(StructBlock):
    text = APIRichTextBlock(
        features=[
            "bold",
            "italic",
            "link",
            "ol",
            "ul",
        ]
    )
