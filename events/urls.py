from django.urls import path
from events.views import event_list, event_detail, event_rsvp, participant_list, contact_page,  participant_dashboard, category_update, category_delete,EventCreateView,EventUpdate,EventDelete,OrganizerDashboard,CategoryCreate

urlpatterns = [
    path('', event_list, name='event_list'),
    path('events/<int:id>/', event_detail, name='event_detail'),
    # path('events/create/', event_create, name='event_create'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    # path('events/<int:id>/update/', event_update, name='event_update'),
    path('events/<int:id>/update/', EventUpdate.as_view(), name='event_update'),
    # path('events/<int:id>/delete/', event_delete, name='event_delete'),
    path('events/<int:pk>/delete/', EventDelete.as_view(), name='event_delete'),
    path('events/<int:id>/rsvp/', event_rsvp, name='event_rsvp'),
    path('participants/', participant_list, name='participant_list'),
    path('contact/', contact_page, name='contact'),
    # path('organizer-dashboard/', organizer_dashboard, name='organizer-dashboard'),
    path('organizer-dashboard/', OrganizerDashboard.as_view(), name='organizer-dashboard'),
    path('participant-dashboard/', participant_dashboard, name='participant-dashboard'),
    # path("category/create/", category_create, name="category_create"),
    path("category/create/", CategoryCreate.as_view(), name="category_create"),
    path("category/<int:id>/update/", category_update, name="category_update"),
    path('category/<int:id>/delete/', category_delete, name='category_delete'),

]
