from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('consent/', views.consent, name='consent'),
    path('lottery/', views.lottery, name='lottery'),
    path('surveyone/', views.surveyOne, name='survey_one'),
    path('surveytwo/', views.surveyTwo, name='survey_two'),
    # path('<int:id>/', views.details, name='details'),
    # path('create', views.create_restaurant, name='create_restaurant'),
    # path('add', views.add_restaurant, name='add_restaurant'),
    # path('review/<int:id>', views.add_review, name='add_review'),
]