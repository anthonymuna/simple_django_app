from django.conf.urls import url
from django.contrib import admin
from .views import index, about, news
from django.conf import settings

urlpatterns = [
	url(r'^$', index),
	url(r'^about/$', about),
	url(r'^news/$', news),
    url(r'^admin/', admin.site.urls),
]
