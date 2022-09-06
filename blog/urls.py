from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', views.post_detail, name='blog_view'),
    path('', views.PostList.as_view(), name='home')
]