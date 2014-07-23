import FGBG.settings
from django.conf.urls import patterns, include, url
from portal.views import *
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^$', index_view),

    url(r'^edit/$', edit_view),

    url(r'^getmask/$', get_mask_view),

    url(r'^show/(?P<img_id>\d+)/$', show_view),
    
) + static(FGBG.settings.STATIC_URL, document_root=FGBG.settings.STATIC_ROOT)

urlpatterns += patterns('',
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': FGBG.settings.MEDIA_ROOT}),
)
