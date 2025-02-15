from django.urls import path
from users.views import signup,user_login,user_logout,admin_dashboard,organizer_dashboard,participant_dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin-dashboard/',admin_dashboard, name='admin_dashboard'),
    path('organizer-dashboard/',organizer_dashboard, name='organizer_dashboard'),
    path('participant-dashboard/',participant_dashboard, name='participant_dashboard'),
]