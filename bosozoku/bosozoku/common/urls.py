from django.urls import path

from bosozoku.common.views import landing_page, about_page


urlpatterns = [
    path('', landing_page, name='index'),
    path('about/', about_page, name='about')
]
