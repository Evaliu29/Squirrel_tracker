from django.urls import path
from . import views

app_name = 'sightings'

urlpatterns = [
        path('', views.lists, name='lists'),
        path('create/',views.create,name='create'),
        path('stats/', views.stats, name='stats'),
        path('<str:squirrel_id>/',views.update,name='update')

        ]
