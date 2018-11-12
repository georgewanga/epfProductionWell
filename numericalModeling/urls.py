from django.urls import path
from numericalModeling import views

app_name = 'numericalModeling'

urlpatterns = [
    path('', views.index_view, name='index'),
]
