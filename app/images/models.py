from app.records.fields import RecordField
from django.conf import settings
from django.db import models
from modelcluster.models import ClusterableModel
from rest_framework.fields import Field
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.models import AbstractImage, AbstractRendition
from wagtail.search import index

DEFAULT_SENSITIVE_IMAGE_WARNING = "This image contains content which some people may find offensive or distressing."


class TranscriptionHeadingChoices(models.TextChoices):
    TRANSCRIPT = "transcript", "Transcript"
    PARTIAL_TRANSCRIPTION = "partial-transcript", "Partial transcript"


class TranslationHeadingChoices(models.TextChoices):
    TRANSLATION = "translation", "Translation"
    MODERN_ENGLISH = "modern-english", "Modern English"


class BaseImage(ClusterableModel, AbstractImage):
    title = models.CharField(
        max_length=255,
        verbose_name="title",
        help_text="The descriptive name of the image. If this image features in a highlights gallery, this title will be visible on the page.",
    )

    copyright = models.CharField(
        verbose_name="copyright",
        blank=True,
        max_length=200,
        help_text="Credit for images not owned by TNA. Do not include the copyright symbol.",
    )

    is_sensitive = models.BooleanField(
        verbose_name="This image is considered sensitive",
        default=False,
        help_text="Tick this if the image contains content which some people may find offensive or distressing. For example, photographs of violence or injury detail.",
    )

    custom_sensitive_image_warning = models.TextField(
        verbose_name="Why might this image be considered sensitive? (optional)",
        help_text='Replaces the default warning message where the image is displayed. For example: "This image has been marked as potentially sensitive because it contains depictions of violence".',
        max_length=200,
        blank=True,
    )

    transcription_heading = models.CharField(
        verbose_name="transcript heading",
        max_length=30,
        choices=TranscriptionHeadingChoices.choices,
        default=TranscriptionHeadingChoices.TRANSCRIPT,
    )

    transcription = RichTextField(
        verbose_name="transcript",
        features=["bold", "italic", "ol", "ul"],
        blank=True,
        max_length=1500,
        help_text="If the image contains text consider adding a transcript.",
    )

    translation_heading = models.CharField(
        verbose_name="translation heading",
        max_length=30,
        choices=TranslationHeadingChoices.choices,
        default=TranslationHeadingChoices.TRANSLATION,
        help_text='If the original transcription language is some earlier form of English, choose "Modern English". If not, choose “Translation”.',
    )

    translation = RichTextField(
        verbose_name="translation",
        features=["bold", "italic", "ol", "ul"],
        blank=True,
        max_length=1500,
        help_text="An optional English / Modern English translation of the transcription.",
    )

    # For Highlights

    record = RecordField(
        verbose_name="related record",
        db_index=True,
        blank=True,
        help_text="If the image relates to a specific record, select that record here.",
    )
    record.wagtail_reference_index_ignore = True

    record_dates = models.CharField(
        verbose_name="record date(s)",
        max_length=100,
        blank=True,
        help_text="Date(s) related to the selected record (max length: 100 chars).",
    )

    description = RichTextField(
        verbose_name="description",
        help_text=(
            "This text will appear in highlights galleries. A 100-300 word "
            "description of the story of the record and why it is significant."
        ),
        blank=True,
        features=["bold", "italic", "link"],
        max_length=900,
    )

    search_fields = AbstractImage.search_fields + [
        index.SearchField("transcription", boost=1),
        index.SearchField("translation", boost=1),
        index.SearchField("description"),
        index.SearchField("copyright"),
        index.FilterField("record"),
        index.FilterField("is_sensitive"),
    ]

    api_fields = [
        APIField("title"),
        APIField("copyright"),
        APIField("description"),
        APIField("transcription_heading"),
        APIField("transcription"),
        APIField("translation_heading"),
        APIField("translation"),
        APIField("record_dates"),
        APIField("record"),
    ]

    @property
    def sensitive_image_warning(self):
        return (
            self.custom_sensitive_image_warning.strip()
            or DEFAULT_SENSITIVE_IMAGE_WARNING
        )

    admin_form_fields = [
        "collection",
        "title",
        "file",
        "copyright",
        "is_sensitive",
        "custom_sensitive_image_warning",
        "tags",
        "focal_point_x",
        "focal_point_y",
        "focal_point_width",
        "focal_point_height",
        "transcription_heading",
        "transcription",
        "translation_heading",
        "translation",
        "record",
        "record_dates",
        "description",
    ]


class BaseImageBasicSerializedField(ImageRenditionField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        return super().to_representation(value) | {
            "title": value.title,
            "description": value.description,
        }


class BaseImageSerializedField(BaseImageBasicSerializedField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        return super().to_representation(value) | {
            "copyright": value.copyright,
            "transcription_heading": value.transcription_heading,
            "transcription": value.transcription,
            "translation_heading": value.translation_heading,
            "translation": value.translation,
            "record_dates": value.record_dates,
            "record": value.record,
            "is_sensitive": value.is_sensitive,
            "custom_sensitive_image_warning": value.custom_sensitive_image_warning,
        }


class BaseImageRendition(AbstractRendition):
    image = models.ForeignKey(
        BaseImage, on_delete=models.CASCADE, related_name="renditions"
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)
