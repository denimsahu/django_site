from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("",views.login_page,name='login'),
    path("home",views.home,name='home'),
    path("home/contact",views.contact_page,name='contact'),
    path("home/link",views.link,name='link'),
    path("signup",views.signup,name='signup'),
    path("logout",views.logout_user,name='logout'),
]
