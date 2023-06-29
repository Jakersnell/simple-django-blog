from django.urls import path
from .views import PostListView, PostDetailView, MakePostView
from . import views

# paths, classes, and functions for routing urlpatterns

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about_view, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('make-post/', MakePostView.as_view(), name='blog-make-post'),
              ]
