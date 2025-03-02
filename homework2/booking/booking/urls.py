"""
URL configuration for booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Zachary Donnelly - CS4300 HW2
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import M_View_Set, S_View_Set, B_View_Set
from . import views
from django.contrib.auth import views as auth_views


#setting up default router
r = DefaultRouter()

#registering view sets for endpoint
r.register(r'Movies', M_View_Set)
r.register(r'Seats', S_View_Set)
r.register(r'Bookings', B_View_Set)

urlpatterns = [
    path('admin/', admin.site.urls),
    #API endpoint
    path('api/', include(r.urls)),
    
    #html paths
    path('movie_list/', views.movie_list, name='movie_list'),
    path('seat_booking/', views.seat_booking, name='seat_booking'),
    path('booking_history/', views.booking_history, name ='booking_history'),
]
