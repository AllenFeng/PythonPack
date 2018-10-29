from django.contrib import admin
from django.conf.urls import url
from blogs import views

admin.autodiscover()

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^$',views.imageZip,name='imageZip'),
]