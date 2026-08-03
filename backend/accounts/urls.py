from django.urls import path
from .import views
urlpatterns=[
    path('userregistration/',views.user_creation,name='register'),
]