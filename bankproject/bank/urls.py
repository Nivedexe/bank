from django.urls import  path
from . import  views
from .views import homepage

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('new/',views.new,name='new'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout, name='logout'),

    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),



]




