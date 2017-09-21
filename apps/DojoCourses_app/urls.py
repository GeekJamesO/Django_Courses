from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'(?P<courseId>\d+)/destroy', views.destroy),
    url(r'(?P<courseId>\d+)/yesDestroy', views.yesDestroy),
    url(r'^addcourse', views.addcourse),
    url(r'^index$', views.index),
    url(r'^$', views.index),
]
