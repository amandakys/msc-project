# experimenttwo/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('', views.camera, name='camera'),
    path('next/', views.next, name='next'),
    # path('filters/', views.filters, name='filters'),
    path ('select/', views.select, name='select_three'),
    path('finished/', views.finished, name='finished'),
    path('retake/', views.retake, name="retake_two")
    # path('complete/', views.complete, name='complete')
]

