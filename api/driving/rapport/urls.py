from django.conf.urls import url

from api.driving.rapport import views

urlpatterns = [
    url(r'^api/driving/rapport/students$', views.GetStudentsApiView.as_view(), name='api-students'),
]