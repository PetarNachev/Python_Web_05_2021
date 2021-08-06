from django.urls import path

from bosozoku.events.views import list_events, event_details, going_event, create_event, edit_event, delete_event, comment_event

urlpatterns = (
    path('', list_events, name='list events'),
    path('details/<int:pk>', event_details, name='event details'),
    path('going/<int:pk>', going_event, name='going event'),
    path('create/', create_event, name='create event'),
    path('edit/<int:pk>', edit_event, name='edit event'),
    path('delete/<int:pk>', delete_event, name='delete event'),
    path('comment/<int:pk>', comment_event, name='comment event'),
)
