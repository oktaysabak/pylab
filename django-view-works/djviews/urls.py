
from django.conf.urls import url, include
from django.contrib import admin
from .views import home, redirect_somewhere

from dashboard.views import DashboardTemplateView, MyView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^redirect/$', redirect_somewhere, name='redirect'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    url(r'myview/', MyView.as_view(), name='myview'),
]
