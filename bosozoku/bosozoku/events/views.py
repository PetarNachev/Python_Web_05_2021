from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, ListView

from bosozoku.common.forms import CommentForm
from bosozoku.events.forms import EventForm, EditEventForm
from bosozoku.events.models import Event, Going


@login_required
def event_details(request, pk):
    event = Event.objects.get(pk=pk)
    event.going_count = event.going_set.count()

    is_creator = event.user == request.user

    is_user_going = event.going_set.filter(user_id=request.user.id) \
        .exists()

    context = {
        'event': event,
        'comment_form': CommentForm(
            initial={
                'event_pk': pk,
            }
        ),
        'comments': event.comment_set.all(),
        'is_creator': is_creator,
        'is_going': is_user_going,
    }

    return render(request, 'events/event_details.html', context)


@login_required
def comment_event(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('event details', pk)


@login_required
def list_events(req):
    all_events = Event.objects.all()

    context = {
        'events': all_events,
    }

    return render(req, 'events/events_list.html', context)


@login_required
def going_event(request, pk):
    event = Event.objects.get(pk=pk)
    user_is_going = event.going_set.filter(user_id=request.user.id) \
        .first()
    if user_is_going:
        user_is_going.delete()
    else:
        going = Going(
            event=event,
            user=request.user,
        )
        going.save()
    return redirect('event details', event.id)


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('list events')
    else:
        form = EventForm()

    context = {
        'form': form,
    }

    return render(request, 'events/event_create.html', context)


class ListEventsView(ListView):
    template_name = 'events/events_list.html'
    context_object_name = 'events'
    model = Event


class EditEventView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'events/event_edit.html'
    form_class = EditEventForm
    # success_url = reverse_lazy('list events')

    def get_success_url(self):
        return reverse('event details', kwargs={
            'pk': self.object.id,
        })


class DeleteEventView(LoginRequiredMixin, DeleteView):
    template_name = 'events/event_delete.html'
    model = Event
    success_url = reverse_lazy('list events')


# @login_required
# def edit_event(req, pk):
#     event = Event.objects.get(pk=pk)
#
#     if req.method == 'POST':
#         form = EditEventForm(req.POST, req.FILES, instance=event)
#         if form.is_valid():
#             form.save()
#             return redirect('list events')
#     else:
#         form = EditEventForm(instance=event)
#
#     context = {
#         'form': form,
#         'event': event
#     }
#     return render(req, 'events/event_edit.html', context)
#
#
# @login_required
# def delete_event(req, pk):
#     event = Event.objects.get(pk=pk)
#
#     if req.method == 'POST':
#         event.delete()
#         return redirect('list events')
#
#     context = {
#         'event': event
#     }
#
#     return render(req, 'events/event_delete.html', context)


