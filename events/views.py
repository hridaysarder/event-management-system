from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to the event management system')

def show_events(request):
    return HttpResponse('Welcome to the show events')

def event_dashboard(request):
    return render(request, "dashboard/event-dashboard.html")
