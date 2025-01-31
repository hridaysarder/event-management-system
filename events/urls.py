from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/<int:id>/update/', views.update_event, name='update_event'),
    path('event/<int:id>/delete/', views.delete_event, name='delete_event'),
    path('dashboard/', views.organizer_dashboard, name='organizer_dashboard'),
    path('search/', views.search_events, name='search_events'),
]
