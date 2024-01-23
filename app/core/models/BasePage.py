from app.images.models import (
    BaseImageBasicSerializedField,
    BaseImageSerializedField,
)
from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.api import APIField
from wagtail.images import get_image_model_string
from wagtail.images.api.fields import ImageRenditionField
from wagtail.models import Page
from wagtail_headless_preview.models import HeadlessPreviewMixin


class BasePage(HeadlessPreviewMixin, Page):
    description = models.TextField(
        max_length=160,
        null=True,
        blank=True,
        help_text="A short, enticing description of this page.",
    )

    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image that will appear on thumbnails and promos around the site.",
    )

    published_date = models.DateField(
        null=True,
        blank=True,
    )

    base_og_title = models.TextField(
        blank=True,
        max_length=160,
    )
    base_og_description = models.TextField(
        blank=True,
        max_length=160,
    )
    base_og_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    facebook_og_title = models.TextField(
        blank=True,
        max_length=160,
    )
    facebook_og_description = models.TextField(
        blank=True,
        max_length=160,
    )
    facebook_og_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    twitter_og_title = models.TextField(
        blank=True,
        max_length=160,
    )
    twitter_og_description = models.TextField(
        blank=True,
        max_length=160,
    )
    twitter_og_author = models.TextField(
        blank=True,
        max_length=160,
    )
    twitter_og_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + []

    meta_content_panels = [
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("published_date"),
    ]

    og_content_panels = [
        MultiFieldPanel(
            [
                FieldPanel("base_og_title"),
                FieldPanel("base_og_description"),
                FieldPanel("base_og_image"),
            ],
            heading="Base Opengraph data",
        ),
        MultiFieldPanel(
            [
                FieldPanel("facebook_og_title"),
                FieldPanel("facebook_og_description"),
                FieldPanel("facebook_og_image"),
            ],
            heading="Facebook Opengraph data",
        ),
        MultiFieldPanel(
            [
                FieldPanel("twitter_og_title"),
                FieldPanel("twitter_og_description"),
                FieldPanel("twitter_og_author"),
                FieldPanel("twitter_og_image"),
            ],
            heading="Twitter Opengraph data",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(meta_content_panels, heading="Meta"),
            ObjectList(og_content_panels, heading="Open Graph"),
            ObjectList(Page.promote_panels, heading="Promote"),
        ]
    )

    api_fields = [
        APIField("image", serializer=ImageRenditionField("fill-600x400")),
        APIField(
            "facebook_og_image",
            serializer=BaseImageBasicSerializedField("fill-1200x630"),
        ),
        APIField(
            "twitter_og_image",
            serializer=BaseImageSerializedField("fill-1200x630"),
        ),
    ]

    # promote_panels = Page.promote_panels = [
    #     FieldPanel("description"),
    #     FieldPanel("image"),
    #     MultiFieldPanel(
    #         [
    #             FieldPanel("base_og_title"),
    #             FieldPanel("base_og_description"),
    #         ],
    #         heading="Base Opengraph data",
    #     ),
    # ]

    # parent_page_types = []
    subpage_types = []