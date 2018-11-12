from django.urls import path
from mercuryManometer import views

app_name = 'mercuryManometer'

urlpatterns = [
    path('', views.index_view, name='index'),
]
