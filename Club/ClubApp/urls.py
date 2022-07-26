from django.urls import path
from ClubApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home_link'),
    path('AddEvent', views.add_event, name='add_event_link'),
    path('EventDetails/<event_id>', views.event_details, name='event_details_link'),
    path('Search', views.search, name='search_events_link'),
    path('UpdateEvent/<event_id>', views.update_event, name='update_event_link'),
    path('DeleteEvent/<event_id>', views.delete_event, name='delete_event_link'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)