"""
URL configuration for vehiclemart project.

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
from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicle_add/',views.VehicleCreateView.as_view(),name="vehicle_add"),
    path('vehicle_list/',views.VehicleListView.as_view(),name="vehicle_list"),
    path('vehicle/<int:pk>/',views.VehicleDetailView.as_view(),name="vehicle_detail"),
    path('vehicle/<int:pk>/remove/',views.VehicleDeleteView.as_view(),name="vehicle_delete"),
    path('vehicle/<int:pk>/change/',views.VehicleUpdateView.as_view(),name="vehicle_update")
]
