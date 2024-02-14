from app.images.blocks import APIImageChooserBlock
from django.utils.safestring import mark_safe
from wagtail.blocks import CharBlock, RichTextBlock, StructBlock


class Picture(StructBlock):
    image = APIImageChooserBlock(
        {
            "jpg": "max-900x900|format-jpeg|jpegquality-80",
            "webp": "max-900x900|format-webp|webpquality-80",
        },
        required=False,
    )

    alt_text = CharBlock(
        max_length=100,
        label="Image alternative text",
        help_text=mark_safe(
            "Alternative (alt) text describes images when they fail to load, and is read aloud by assistive "
            "technologies. Use a maximum of 100 characters to describe your image. Decorative images do not "
            'require alt text. <a href="https://html.spec.whatwg.org/multipage/images.html#alt" target="_blank">'
            "Check the guidance for tips on writing alt text</a>."
        ),
        required=False,
    )

    caption = RichTextBlock(
        features=["bold", "italic", "link"],
        help_text=(
            "An optional caption for non-decorative images, which will be displayed directly below the image. "
            "This could be used for image sources or for other useful metadata."
        ),
        label="Caption (optional)",
        required=False,
    )
