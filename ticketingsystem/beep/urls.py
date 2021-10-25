from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('features/', views.features),
    path('about/', views.about),
    path('contact/', views.contact),
    path('signin/', views.signin.as_view(), name = "user_info"),
    path('signup/', views.signup),
    path('dashboard/', views.dashboard.as_view(), name = "dashboard_info")
]
