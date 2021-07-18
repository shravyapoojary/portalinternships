"""interns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('index/', views.homepage, name='index'),
     path('signup/', views.signup, name='usersignup'),
   path('apply/', views.internship, name='apply'),
                  path('login/', views.loginpage, name='login'),
                  path('company/', views.companypage, name='company'),
                  path('course/', views.coursepage, name='courses'),
                  path('companysignup/', views.companysignup, name='companysignup'),
                  path('companylogin/', views.companyloginpage, name='companylogin'),
                  path('userdashboard/', views.userdashboardpage, name='userdashboard'),
                  path('logout/', views.userlogout, name='logout'),
                  path('intern/', views.internpage, name='intern'),
                  path('blog/', views.blogpage, name='blog'),
                  path('blog_detail/<int:pk>/', views.blogDetailView.as_view(), name='blog_detail'),
                  path('contact/', views.contactinfo, name='contact'),
                  path('profile/', views.profilepage, name='profile'),
                  path('reset_password/',
                       auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
                       name="reset_password"),

                  path('reset_password_sent/',
                       auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
                       name="password_reset_done"),

                  path('reset/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
                       name="password_reset_confirm"),

                  path('reset_password_complete/',
                       auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
                       name="password_reset_complete"),
              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
