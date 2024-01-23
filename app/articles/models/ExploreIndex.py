from app.core.models import BasePage


class ExploreIndex(BasePage):
    subpage_types = ["core.IndexPage", "articles.ArticlesIndex"]
