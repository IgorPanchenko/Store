from django.urls import path
from users import views


urlpatterns = [
    path('login/', views.login_1, name='login'),
    path('registration/', views.registration, name='register'),
    path('profile/', views.profile, name='profile'),
]