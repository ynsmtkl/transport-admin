from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/users/login$', views.UserLoginApiView.as_view(), name='api-login'),
    url(r'^api/users/verify$', views.VerifyUserApiView.as_view(), name='api-verify')
]