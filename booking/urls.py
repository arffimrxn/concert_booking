from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.concert_list, name='concert_list'),
    path('register/', views.register, name='register'),
    
    # We use Django's built-in auth views for secure login/logout
    path('login/', auth_views.LoginView.as_view(template_name='booking/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('book/<int:concert_id>/', views.book_ticket, name='book_ticket'),
    path('profile/', views.profile, name='profile'),
    path('welcome/', views.welcome_page, name='welcome'),
]