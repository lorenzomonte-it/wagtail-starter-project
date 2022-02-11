from django.db import models
from wagtail.core.models import Page


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]

    def get_admin_display_title(self):
        return "Homepage"
