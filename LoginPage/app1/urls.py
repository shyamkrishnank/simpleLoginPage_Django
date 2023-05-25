from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.user_Login, name = 'user_login'),
    path('home/',views.Home, name = 'home'),
    path('user_logout/',views.user_logout, name='user_logout')
]