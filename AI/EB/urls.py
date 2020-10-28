from django.urls import path

from . import views

app_name = 'EB'
urlpatterns = [
    path('', views.billinfoview, name='billinfo'),
    path('waiting/', views.processingview, name='processing'),
]