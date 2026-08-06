from django.urls import path
from .import views
urlpatterns=[
    path('userregistration/',views.user_creation,name='register'),
    path('home/',views.homepage,name='homepage'),
    path('',views.login_view,name='login'),
]