from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/users/register$', views.UserRegisterApiView.as_view(), name='api-register'),
    url(r'^api/users/secret$', views.SecretValidationApiView.as_view(), name='api-secret')
]