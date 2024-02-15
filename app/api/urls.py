from app.core.models import BasePage
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail_headless_preview.models import PagePreview
from wagtailmedia.api.views import MediaAPIViewSet


class PagePreviewAPIViewSet(PagesAPIViewSet):
    known_query_parameters = PagesAPIViewSet.known_query_parameters.union(
        ["content_type", "token"]
    )

    def listing_view(self, request):
        page = self.get_object()
        serializer = self.get_serializer(page)
        return Response(serializer.data)

    def detail_view(self, request, pk):
        page = self.get_object()
        serializer = self.get_serializer(page)
        return Response(serializer.data)

    def get_object(self):
        app_label, model = self.request.GET["content_type"].split(".")
        content_type = ContentType.objects.get(app_label=app_label, model=model)

        page_preview = PagePreview.objects.get(
            content_type=content_type, token=self.request.GET["token"]
        )
        page = page_preview.as_page()
        if not page.pk:
            # fake primary key to stop API URL routing from complaining
            page.pk = 0

        return page


class CustomPagesAPIViewSet(PagesAPIViewSet):
    model = BasePage

    meta_fields = PagesAPIViewSet.meta_fields + [
        "description",
        "image",
        "image_webp",
        "published_date",
        "base_og_title",
        "base_og_description",
        "base_og_image",
        "facebook_og_title",
        "facebook_og_description",
        "facebook_og_image",
        "twitter_og_title",
        "twitter_og_description",
        "twitter_og_author",
        "twitter_og_image",
    ]

    listing_default_fields = PagesAPIViewSet.listing_default_fields + [
        "description",
        "image",
        "published_date",
    ]


class CustomImagesAPIViewSet(ImagesAPIViewSet):
    body_fields = ImagesAPIViewSet.body_fields + [
        # "collection",
        "title",
        "file",
        "copyright",
        "is_sensitive",
        "custom_sensitive_image_warning",
        "tags",
        "transcription_heading",
        "transcription",
        "translation_heading",
        "translation",
        "record",
        "record_dates",
        "description",
    ]


api_router = WagtailAPIRouter("wagtailapi")

api_router.register_endpoint("pages", CustomPagesAPIViewSet)
api_router.register_endpoint("images", CustomImagesAPIViewSet)
api_router.register_endpoint("media", MediaAPIViewSet)
api_router.register_endpoint("page_preview", PagePreviewAPIViewSet)
