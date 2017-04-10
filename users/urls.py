from django.conf.urls import url
from .views import LoginView, register, profile_page, update_profile
from django.contrib.auth.views import (logout,logout_then_login, password_change, password_change_done,
                                        password_reset, password_reset_done, password_reset_confirm,
                                        password_reset_complete)
urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^register/$', register, name='register'),
    #Change password urls
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change-done/$', password_change_done, name='password_change_done'),
    #Reset password urls
    url(r'^password-reset/$', password_reset, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),
    #User
    url(r'^profile/(?P<username>\w+)/$', update_profile, name='Profile'),
    url(r'profile/edit/$', update_profile, name='profile_update'),

]
