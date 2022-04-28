from django.urls import path,include
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.showLoginPage,name='login'), 
    path('post/ajax/loginUser',views.login_request,name='loginUser'),
   
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('change_password/', views.change_password, name='change_password'), 
   
    path('activation_sent/',views.account_activation_sent,name='activation_sent'),
    path('activate/<uid>/<token>/', views.activate, name='activate'),
   
]
