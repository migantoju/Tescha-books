from django.conf.urls import url
from .views import LoginView
from django.contrib.auth.views import logout,logout_then_login, password_change, password_change_done
urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    #Change password urls
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change-done/$', password_change_done, name='password_change_done'),

]
