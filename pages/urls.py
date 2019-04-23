from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserRegisterSerializer)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    url(r'^get_session_id$', views.get_session, name='session_id'),
    url(r'^get_token$', views.get_token, name='token'),

    url(r'^login$', views.UserLoginApiView.as_view(), name='login'),
    url('register/', views.UserRegisterSerializer.as_view(), name='register'),

]