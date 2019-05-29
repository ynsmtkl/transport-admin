from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/driving/profile/parent$', views.EditUserApiView.as_view(), name='api-profile-parent'),
    url(r'^api/driving/profile/driver', views.EditDriverApiView.as_view(), name='api-profile-driver'),
    url(r'^api/driving/profile/student', views.EditStudentApiView.as_view(), name='api-profile-student'),
]