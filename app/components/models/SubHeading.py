from wagtail.blocks import CharBlock, StructBlock


class SubHeading(StructBlock):
    text = CharBlock(
        max_length=100,
        label="Heading",
        required=True,
    )
