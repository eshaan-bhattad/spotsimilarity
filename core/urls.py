from django.urls import path
from . import views

urlpatterns= [
	path('', views.index, name="index"),
	path('about', views.about, name="about"),
	path('comparison', views.comparison, name="comparison"),
	path('loading', views.loading, name="loading")
]
