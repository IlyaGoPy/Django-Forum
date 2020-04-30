from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
	path('login/', views.log_in, name = 'login'),
    path('register/', views.register, name = 'register'),
]
