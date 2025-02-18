from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from django.utils import timezone
from events.models import Event, Category
from events.forms import EventForm
from django.contrib.auth.decorators import login_required, user_passes_test

def event_list(request):
    events = Event.objects.select_related(
        'category').prefetch_related('participants').all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})


def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})


def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


def organizer_dashboard(request):
    # total_participants = Participant.objects.count()
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(
        date__gte=timezone.now().date()).count()
    past_events = Event.objects.filter(date__lt=timezone.now().date()).count()
    today_events = Event.objects.filter(date=timezone.now().date())

    return render(request, 'events/dashboard.html', {
        # 'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'today_events': today_events,
    })


def search_events(request):
    query = request.GET.get('q')
    if query:
        events = Event.objects.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )
    else:
        events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user not in event.rsvp_users.all():
        event.rsvp_users.add(request.user)
    return redirect('event_list')