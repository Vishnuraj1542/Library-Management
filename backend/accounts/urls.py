from django.urls import path
from .import views
urlpatterns=[
    path('userregistration/',views.user_creation,name='register'),
    path('home/',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
]