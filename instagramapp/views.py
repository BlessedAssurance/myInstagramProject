# from django.http  import HttpResponse
from django.urls import reverse_lazy
from .forms import CreatePostForm, CreateCommentForm
from .models import Post, Comment
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomePageView(ListView):
    model = Comment
    success_url = reverse_lazy('home')
    model = Post
    form_class= CreateCommentForm
    template_name = 'instagramapp/index.html'
    context_object_name = 'posts'
    ordering =['-date_posted']

