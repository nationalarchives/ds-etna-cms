from .BasePage import BasePage


class HomePage(BasePage):
    subpage_types = ["articles.ExploreIndex", "authors.Authors"]
