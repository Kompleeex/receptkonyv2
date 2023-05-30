from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'fooldal'),
    path('upload/', views.receptUpload, name='feltoltes'),
    path('delete/<int:id>/', views.receptDelete, name='torles')

]


