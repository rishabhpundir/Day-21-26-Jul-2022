from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ClubApp.models import Event
from templates.event_form import EventForm

# Create your views here.
def home(request):
    events_list = Event.objects.all()
    return render(request, 'home.html', {'events':events_list})

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/AddEvent?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_event.html', {'form':form, 'submitted':submitted})

def event_details(request, event_id):
    updated = False
    event = Event.objects.get(pk=event_id)
    if 'updated' in request.GET:
            updated = True
    return render(request, 'event_details.html', {'event': event, 'updated':updated})


def search(request):
    if request.method == "POST":
        search_query = request.POST['search-bar']
        events = Event.objects.filter(event_name__contains=search_query)
        return render(request, 'search.html', {'search_query':search_query, 'events': events})
    else:
        return render(request, 'search.html', {})

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    updated = False
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f'/EventDetails/{event_id}?updated=True')
    return render(request, 'update_event.html', {'event': event, 'form': form})

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return HttpResponseRedirect('/')
