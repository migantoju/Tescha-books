from django.conf.urls import url
from .views import LoginView
from django.contrib.auth.views import logout,logout_then_login
urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
]
