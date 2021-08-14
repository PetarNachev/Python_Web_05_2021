from django.urls import path

from bosozoku.common.views import landing_page, about_page, edit_comment, delete_comment

urlpatterns = [
    path('', landing_page, name='index'),
    path('about/', about_page, name='about'),
    path('comment_edit/<int:pk>', edit_comment, name='edit comment'),
    # path('comment_edit/<int:pk>', EditCommentView.as_view(), name='edit comment'),
    path('comment_delete/<int:pk>', delete_comment, name='delete comment'),
]
