from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='browse_home')
]