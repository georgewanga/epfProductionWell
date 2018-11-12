from django.urls import path
from dataLoggers import views

app_name = 'dataLoggers'

urlpatterns = [
    path('', views.index_view, name='index'),
]
