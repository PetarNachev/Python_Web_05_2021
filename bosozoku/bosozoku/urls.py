from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bosozoku.common.urls')),
    path('accounts/', include('bosozoku.accounts.urls')),
    path('events/', include('bosozoku.events.urls')),
]
