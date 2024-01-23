from app.images.models import BaseImageSerializedField
from wagtail.images.blocks import ImageChooserBlock


class APIImageChooserBlock(ImageChooserBlock):
    def __init__(
        self,
        filter_spec="fill-600x400",
        required=True,
        help_text=None,
        validators=(),
        **kwargs,
    ):
        self._filter_spec = filter_spec
        self._required = required
        self._help_text = help_text
        self._validators = validators
        super().__init__(**kwargs)

    def get_api_representation(self, value, context=None):
        return BaseImageSerializedField(self._filter_spec).to_representation(
            value
        )
