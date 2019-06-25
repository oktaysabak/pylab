
from django.conf.urls import url
from django.contrib import admin

from accounts.views import register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', register),
]
