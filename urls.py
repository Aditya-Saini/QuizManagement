from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='QuizManagement'),
    path('test/', views.test, name="quiz"),
    
]
