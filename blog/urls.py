from django.urls import path
from . import views

urlpatterns = [
               path('create', views.create, name='create'),
               path('', views.allblogs, name='allblogs'),
               path('<int:blog_id>/', views.detail, name='detail'),
              ]