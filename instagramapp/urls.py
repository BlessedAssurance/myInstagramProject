from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import HomePageView, PostDetailView, PostCreateView

urlpatterns=[
    url(r'^$',HomePageView.as_view(),name = 'home'),
    url(r'^post/<int:pk>$',PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new$',PostCreateView.as_view(), name='post_create')
]

if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)