from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'catalog'

urlpatterns = [
    path('home/', views.index, name="index"),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='catalog/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('my_dashboard/', views.my_dashboard, name='my_dashboard'),
]
