from django.urls import path
from assumptions import views

urlpatterns =[
    path('assumption/', views.create_assumption, name='assumption'),
]