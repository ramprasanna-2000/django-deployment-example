from django.urls import path,include
from login_app import views


app_name = 'login_app'


urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='user_logout')
]
