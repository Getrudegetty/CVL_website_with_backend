from django.urls import path
from . import views

app_name = 'cvl_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]