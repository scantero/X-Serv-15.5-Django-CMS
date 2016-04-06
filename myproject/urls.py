from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cms.views.mostrarContenido'),
    url(r'^(\d+)$', 'cms.views.mostrarPagina'),
    url(r'^nuevocontenido/(.+)\/(.+)$', 'cms.views.nuevoContenido'),
    url(r'^admin/', include(admin.site.urls)),
)
