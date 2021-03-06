"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import index_view, product_view, add_product, product_delete, product_update, product_search, product_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('product/<int:pk>', product_view, name='product_view'),
    path('product/add', add_product, name='add_product'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
    path('product/<int:pk>/edit/', product_update, name='product_update'),
    path('product/<str:cat>', product_category, name='product_category'),
    path('product/search/', product_search, name='product_search'),

]
