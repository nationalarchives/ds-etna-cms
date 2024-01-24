from app.components.models import Blockquote, Hero, Paragraph, Picture
from app.records.blocks import FeaturedRecords
from django.utils.text import slugify
from wagtail.blocks import CharBlock, StreamBlock, StructBlock


class SectionContentBlock(StreamBlock):
    # media = MediaBlock()
    # featured_record_article = FeaturedRecordArticleBlock()
    # promoted_item = PromotedItemBlock()
    # promoted_list = PromotedListBlock()
    blockquote = Blockquote()
    hero = Hero()
    paragraph = Paragraph()
    picture = Picture()
    featured_records = FeaturedRecords()


class SectionBlock(StructBlock):
    heading = CharBlock(max_length=100)
    content = SectionContentBlock(required=False)

    def get_heading_id(self, value):
        return f"h2.{slugify(value['heading'])}"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context["heading_id"] = self.get_heading_id(value)
        return context


class ArticleStreamBlock(StreamBlock):
    content_section = SectionBlock()
