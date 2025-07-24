"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from coin import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('coin/add/', views.add_coin, name='add_coin'),
    path('', views.list_coins, name='list_coins'),
    path('coins/update/<int:coin_id>/', views.update_coin, name='update_coin'),
    path("coins/delete/<int:coin_id>/", views.delete_coin, name="delete_coin"),
    path("coins/search/", views.search_coins, name="search_coin"),
]
