from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, TemplateView

from bosozoku.common.forms import EditCommentForm
from bosozoku.common.models import Comment


class LandingPage(TemplateView):
    template_name = 'index.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


# def landing_page(request):
#     return render(request, 'index.html')

#
# def about_page(request):
#     return render(request, 'about.html')


def edit_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    is_owner = comment.user == request.user

    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('event details', comment.event.id)
    else:
        form = EditCommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment,
        'is_created_by_user': is_owner,
    }
    return render(request, 'comment_edit.html', context)


# class EditCommentView(LoginRequiredMixin, UpdateView):
#     model = Comment
#     template_name = 'comment_edit.html'
#     form_class = EditCommentForm
#     # success_url = reverse_lazy('list events')
#
#     def get_success_url(self):
#         return reverse('event details', kwargs={
#             'pk': self.object.event.id,
#         })


# def delete_comment(request, pk):
#     comment = Comment.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         comment.delete()
#         return redirect('event details', comment.event.id)
#
#     context = {
#         'comment': comment
#     }
#
#     return render(request, 'comment_delete.html', context)


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    template_name = 'comment_delete.html'
    model = Comment
    # success_url = reverse_lazy('list events')

    def get_success_url(self):
        return reverse('event details', kwargs={
            'pk': self.object.event.id,
        })
