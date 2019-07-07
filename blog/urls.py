from django.conf.urls import url
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  url(r'^$', views.home, name='home'),
                  url('list', views.list_post, name='list_post'),
                  url('new', views.create_post, name='new_post'),
                  url(r'^delete/(?P<pk>[\d]+)/$', views.delete_post, name='delete_post'),
                  url(r'^view/(?P<pk>[\d]+)/$', views.view_post, name='view_post'),
                  url(r'^edit/(?P<pk>[\d]+)/$', views.edit_post, name='edit_post'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
