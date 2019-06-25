
from django.conf.urls import url
from django.contrib import admin

from accounts.views import register, user_login, user_logout, home

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^admin/', admin.site.urls, name="amdin"),
    url(r'^register/', register, name="register"),
    url(r'^login/', user_login, name="login"),
    url(r'^logout/', user_logout, name="logout"),
]
