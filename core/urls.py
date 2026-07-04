from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
    path('properties/<int:property_pk>/apply/', views.apply_to_property, name='apply_to_property'),
    path('application/success/', views.application_success, name='application_success'),
    path('register/', views.create_owner, name='create_owner'),
    path('register/<int:owner_id>/cat/', views.create_cat, name='create_cat'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('setup-admin/', views.create_admin, name='create_admin'),
]