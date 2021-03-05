from django.db import models

from wagtail.core.models import Page

from stream_blocks import blocks


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]

    def get_admin_display_title(self):
        return "Homepage"


''' Pagina cartella '''
# class FolderPage(Page):
#     show_in_menus_default = True
#     parent_page_types = ['home.HomePage', 'home.FolderPage']

#     class Meta:
#         verbose_name = 'Cartella'


''' Pagina singola '''
# class SinglePage(Page):
#     show_in_menus_default = True
#     parent_page_types = ['home.HomePage', 'home.FolderPage']

#     class Meta:
#         verbose_name = 'Pagina'
