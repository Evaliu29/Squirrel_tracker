from django.urls import path
from . import views

app_name = 'sightings'

urlpatterns = [
        path('', views.lists, name='lists'),
        path('<str:squirrel_id>/',views.update,name='update'),

        ]
