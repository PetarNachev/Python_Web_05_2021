from django.shortcuts import render, redirect

# Create your views here.
from bosozoku.common.forms import EditCommentForm
from bosozoku.common.models import Comment


def landing_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


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


def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('event details', comment.event.id)

    context = {
        'comment': comment
    }

    return render(request, 'comment_delete.html', context)
