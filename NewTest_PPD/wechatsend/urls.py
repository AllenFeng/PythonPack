from django.contrib import admin
from django.conf.urls import url
from wechatsend import views

admin.autodiscover()

urlpatterns = [
    url(r'^$',views.index,name='index'),
]