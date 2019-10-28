from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    path('jobs/', views.job_list),
    path('jobs/<int:pk>', views.job_detail),
}

urlpatterns = format_suffix_patterns(urlpatterns)