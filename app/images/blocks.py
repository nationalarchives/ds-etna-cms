from app.images.models import BaseImageSerializedField
from wagtail.images.blocks import ImageChooserBlock


class APIImageChooserBlock(ImageChooserBlock):
    def __init__(
        self,
        filter_specs="fill-600x400",
        required=True,
        help_text=None,
        validators=(),
        **kwargs,
    ):
        self._filter_specs = filter_specs
        self._required = required
        self._help_text = help_text
        self._validators = validators
        super().__init__(**kwargs)

    def get_api_representation(self, value, context=None):
        if type(self._filter_specs) is dict:
            images = {}
            for filter_spec in self._filter_specs:
                images[filter_spec] = BaseImageSerializedField(
                    self._filter_specs[filter_spec]
                ).to_representation(value)
            return images
        else:
            return BaseImageSerializedField(
                self._filter_specs
            ).to_representation(value)
