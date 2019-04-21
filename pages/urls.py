from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    url(r'^get_session_id$', views.get_session, name='session_id'),
    url(r'^get_token$', views.get_token, name='token'),
    url('userlogged/', views.userlogin, name='userlogged'),
]