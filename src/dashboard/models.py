from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images import get_image_model_string


@register_setting
class WebsiteSettings(BaseSetting):
    """Website settings for our custom website."""

    # Social Links
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
    linkedin = models.URLField(blank=True, null=True, help_text="Linkedin URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")

    # Analytics Scripts
    google_tag_head = models.TextField("Google Tag Manager <head>", blank=True, null=True, help_text=_("Aggiungi lo script di Google Tag Manager per il tag <head></head>"))
    google_tag_body = models.TextField("Google Tag Manager <body>", blank=True, null=True, help_text=_("Aggiungi lo script di Google Tag Manager per il tag <body></body>"))
    google_analytics = models.CharField("Google Analytics Traking ID", max_length=20, blank=True, null=True, help_text=_('Il tuo Google Analytics tracking ID (inizia con "UA-")'))
    facebook_pixel = models.TextField("Facebook Pixel", blank=True, null=True, help_text=_("Aggiungi lo script di Facebook Pixel"))

    # Branding
    logo = models.ForeignKey(
        get_image_model_string(),
        null=True, blank=True, on_delete=models.SET_NULL, related_name='logo',
        verbose_name='Logo',
        help_text=_("Brand logo per tutto il sito")
    )
    favicon = models.ForeignKey(
        get_image_model_string(),
        null=True, blank=True, on_delete=models.SET_NULL, related_name='favicon',
        verbose_name='Favicon'
    )

    # Tab Panels
    brand_tab_panels = [
        MultiFieldPanel([
            ImageChooserPanel("logo"),
            ImageChooserPanel("favicon"),
        ], heading="Branding"),
    ]
    social_tab_panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("instagram"),
            FieldPanel("linkedin"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ], heading="Social media Links")
    ]
    analytics_tab_panels = [
        MultiFieldPanel([
            FieldPanel("google_tag_head", widget=forms.Textarea(attrs={'rows': 6})),
            FieldPanel("google_tag_body", widget=forms.Textarea(attrs={'rows': 6})),
        ], heading="Google Tag Manager"),

        MultiFieldPanel([
            FieldPanel("google_analytics"),
            FieldPanel("facebook_pixel", widget=forms.Textarea(attrs={'rows': 5})),
        ], heading="Analytics")
    ]

    edit_handler = TabbedInterface([
        ObjectList(brand_tab_panels, heading='Branding'),
        ObjectList(social_tab_panels, heading='Social Media'),
        ObjectList(analytics_tab_panels, heading='Analytics'),
    ])

    class Meta:
        verbose_name = "Generale"
        verbose_name_plural = "Generale"
