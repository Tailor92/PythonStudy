from django.urls import path

from . import views

# pybo에서 생성된 경로 관리
urlpatterns = [
    path('', views.index),
]