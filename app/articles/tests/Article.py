import json

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from wagtail.models import Site

from ..models.Article import Article


class TestArticlePageSectionBlockIntegration(TestCase):
    pass

    # def setUp(self):
    #     root = Site.objects.get().root_page

    #     self.article_page = Article(
    #         id=99999,
    #         title="Test",
    #         content_type=ContentType.objects.get(
    #             app_label="articles", model="Article"
    #         ),
    #         body=json.dumps(
    #             [
    #                 {
    #                     "type": "content_section",
    #                     "value": {
    #                         "heading": "Heading",
    #                         "content": [
    #                             {
    #                                 "type": "paragraph",
    #                                 "value": {
    #                                     "text": "<p>Welcome</p>",
    #                                 },
    #                             }
    #                         ],
    #                     },
    #                 }
    #             ]
    #         ),
    #     )
    #     root.add_child(instance=self.article_page)

    # def test_api(self):
    #     response = self.client.get(self.article_page.get_url())
    #     self.assertNotContains(response, "jumplinks")
