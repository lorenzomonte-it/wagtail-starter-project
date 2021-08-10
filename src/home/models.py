from django.db import models
from wagtail.core.models import Page


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]

    def get_admin_display_title(self):
        return "Homepage"


''' Esempio Pagina singola '''
# class SinglePage(Page):
#     show_in_menus_default = True
#     parent_page_types = ['home.HomePage', 'home.FolderPage']

#     class Meta:
#         verbose_name = 'Pagina'
