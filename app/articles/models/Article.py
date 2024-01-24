from app.articles.blocks import ArticleStreamBlock
from app.core.models import BasePage
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField


class Article(BasePage):
    subpage_types = []

    body = StreamField(
        ArticleStreamBlock, blank=True, null=True, use_json_field=True
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("body"),
    ]

    api_fields = BasePage.api_fields + [
        APIField("body"),
    ]
