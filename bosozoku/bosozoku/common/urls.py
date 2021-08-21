from django.urls import path

from bosozoku.common.views import edit_comment, DeleteCommentView, LandingPage, AboutPage

urlpatterns = [
    # path('', landing_page, name='index'),
    path('', LandingPage.as_view(), name='index'),
    # path('about/', about_page, name='about'),
    path('about/', AboutPage.as_view(), name='about'),
    path('comment_edit/<int:pk>', edit_comment, name='edit comment'),
    # path('comment_edit/<int:pk>', EditCommentView.as_view(), name='edit comment'),
    # path('comment_delete/<int:pk>', delete_comment, name='delete comment'),
    path('comment_delete/<int:pk>', DeleteCommentView.as_view(), name='delete comment'),
]
