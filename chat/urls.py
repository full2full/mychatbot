from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chat-home'),
    path('get-response/', views.get_response, name='chat-response'),
]
