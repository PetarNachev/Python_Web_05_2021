from django.urls import path
from bosozoku.accounts.views import logout_user, profile_details, list_profiles, \
    RegisterView, ProfileDetailsView, LoginUserView

urlpatterns = (
    # path('login/', login_user, name='log in user'),
    path('login/', LoginUserView.as_view(), name='log in user'),
    path('logout/', logout_user, name='log out user'),
    # path('register/', register_user, name='register user'),
    path('register/', RegisterView.as_view(), name='register user'),
    # path('login/', LoginUserView.as_view(), name='log in user'),
    # path('profile/', profile_details, name='profile details'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile_list/', list_profiles, name='profile list'),
)
