from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.views import defaults as default_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from wagtail.contrib.sitemaps.views import sitemap

from . import views as wagtail_project_views

from search import views as search_views

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('search/', search_views.search, name='search'),
]


urlpatterns = urlpatterns + [
    path('robots.txt', wagtail_project_views.RobotsView.as_view(), name='robots'),
    path('sitemap.xml', sitemap),

    path("", include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        # Testing 404/500 page on development
        path('404/', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        path('500/', default_views.server_error),
    ] + urlpatterns
