from django.urls import path
from events.views import show_events, event_dashboard

urlpatterns = [
    path('show-events/', show_events),
    path('event-dashboard/', event_dashboard)
]
