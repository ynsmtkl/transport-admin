from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('connects', views.ConnectView)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('connects/', include(router.urls)),

    url(r'^get_session_id$', views.get_session, name='session_id'),
    url(r'^get_token$', views.get_token, name='token'),
    url('userlogged/', views.userlogin, name='userlogged'),

    url(r'^login$', views.UserLoginApiView.as_view(), name='login'),
    url(r'^register$', views.UserRegisterSerializer.as_view(), name='register'),

]