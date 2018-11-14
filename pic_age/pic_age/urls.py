from django.conf.urls import patterns, include, url

from django.contrib import admin
from pic.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pic_age.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',upload),
    url(r'^uploadImg',uploadImg),
    url(r'',upload),
)
