from wagtail.blocks import RichTextBlock, StructBlock
from wagtail.rich_text import expand_db_html


class APIRichTextBlock(RichTextBlock):
    def get_api_representation(self, value, context=None):
        representation = super().get_api_representation(value, context)
        return expand_db_html(representation)
