from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING

app_name = 'myapp'

urlpatterns = [
    url(r'^relative/$',views.relative, name = 'relative'),
    url(r'other/$',views.other, name = 'other'),
]