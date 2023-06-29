from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


# using register as '/' base view until user/ myaccount exists

urlpatterns = [
    path('register/', views.register_view, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
    path('myprofile/', views.myprofile_view, name='user-myprofile'),
    path('myprofile/edit', views.edit_myprofile_view, name='user-edit-myprofile'),
              ]
