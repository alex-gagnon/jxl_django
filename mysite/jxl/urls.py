from django.urls import path

from . import views

app_name = 'jxl'
urlpatterns = [
    # ex: /jxl/
    path('', views.HomeView.as_view(), name='home')
]
