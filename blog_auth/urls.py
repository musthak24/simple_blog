from django.conf.urls import url
from blog_auth import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^login/$', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_view.LogoutView.as_view(), name='logout'),
    url(r'^sign_up/$', views.CreateSignup.as_view(), name='sign_up'),
]
