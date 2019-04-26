from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/users/login$', views.UserLoginApiView.as_view(), name='api-login')
]