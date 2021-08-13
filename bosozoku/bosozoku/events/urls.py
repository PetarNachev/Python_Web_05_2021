from django.urls import path

from bosozoku.events.views import list_events, event_details, going_event, create_event, \
    comment_event, DeleteEventView, EditEventView, ListEventsView

urlpatterns = (
    path('', ListEventsView.as_view(), name='list events'),
    path('details/<int:pk>', event_details, name='event details'),
    path('going/<int:pk>', going_event, name='going event'),
    path('create/', create_event, name='create event'),
    # path('edit/<int:pk>', edit_event, name='edit event'),
    path('edit/<int:pk>', EditEventView.as_view(), name='edit event'),
    # path('delete/<int:pk>', delete_event, name='delete event'),
    path('delete/<int:pk>', DeleteEventView.as_view(), name='delete event'),
    path('comment/<int:pk>', comment_event, name='comment event'),
)
