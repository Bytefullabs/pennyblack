from django.conf.urls import url

from pennyblack.views import redirect_link, proxy, view, ping

urlpatterns = (
    url(r'^link/(?P<mail_hash>[^/]+)/(?P<link_hash>[a-z0-9]+)/$', redirect_link, name='pennyblack.redirect_link'),
    url(r'^proxy/(?P<mail_hash>[^/]+)/(?P<link_hash>[a-z0-9]+)/$', proxy, name='pennyblack.proxy'),
    url(r'^view/(?P<mail_hash>\w+)', view, name='pennyblack.view'),
    url(r'^ping/(?P<mail_hash>\w*)/(?P<filename>.*)$', ping, name='pennyblack.ping'),
)
