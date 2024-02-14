from app.components.blocks import APIRichTextBlock
from app.core.models import BasePage
from django.utils.functional import cached_property

# from django.db.models import ForeignKey, SET_NULL
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.blocks import CharBlock

# from wagtail.images import get_image_model_string
from wagtail.images.api.fields import ImageRenditionField


class Authors(BasePage):
    subpage_types = ["authors.Author"]

    @cached_property
    def author_pages(self):
        """Return a sample of child pages for rendering in teaser."""
        return (
            self.get_children().type(Author).order_by("name").live().specific()
        )


class Author(BasePage):
    name = CharBlock(
        max_length=100,
        label="Name",
    )

    role = CharBlock(
        max_length=250,
        label="Role",
    )

    # image = ForeignKey(
    #     get_image_model_string(),
    #     blank=True,
    #     null=True,
    #     on_delete=SET_NULL,
    #     related_name="+",
    # )

    introduction = APIRichTextBlock(
        features=[
            "bold",
            "italic",
            "link",
            "ol",
            "ul",
        ]
    )

    content_panels = BasePage.content_panels + [
        # FieldPanel("name"),
        # FieldPanel("role"),
        # FieldPanel("introduction"),
    ]

    api_fields = BasePage.api_fields + [
        APIField("name"),
        APIField("role"),
        APIField("introduction"),
        APIField("image", serializer=ImageRenditionField("fill-600x400")),
    ]
