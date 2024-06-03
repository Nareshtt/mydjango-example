from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'sign_up'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout, name='logout'),
]