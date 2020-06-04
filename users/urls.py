from django.urls import url
from .views import SignUpView,ProfilePageView, ProfileEditPageView

urlpatterns = [
    url(r'', SignUpView.as_view(), name='signup'),
    url(r'profile/$', ProfilePageView.as_view(), name='profile'),
    url(r'profile_edit/$', ProfileEditPageView, name='profile_edit')
]