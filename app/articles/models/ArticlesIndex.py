from app.core.models import BasePage


class ArticlesIndex(BasePage):
    subpage_types = ["articles.Article", "articles.FocusedArticle"]
