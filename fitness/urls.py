from django.urls import  path
from fitness import views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('index',views.index,name='index'),
  path('about',views.about,name='about'),
  path('contact',views.contact,name='contact'),
  path('services',views.services,name='services'),
  path('login',auth_views.LoginView.as_view(),name='login'),
  path('logout',auth_views.LogoutView.as_view(),name='logout'),
  path('register',views.register,name='register'),
  path('home',views.home,name='home'),
  path('adminservices',views.admin_services,name='admin_services'),
  path('delete/<int:id>/',views.delete,name='delete'),
  path('update/<int:id>/', views.update, name='update')







]