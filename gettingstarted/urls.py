from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import kevinbacon.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', kevinbacon.views.index, name='index'),
    url(r'^input', kevinbacon.views.input, name='input'),
    url(r'^admin/', include(admin.site.urls)),

)
