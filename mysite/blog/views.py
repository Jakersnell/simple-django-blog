from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, View
from .models import Post
from .forms import MakePostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin






def home_view(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'home',
    }
    return render(request, 'blog/home.html', context)


def about_view(request):

    return render(request, 'blog/about.html', {'title': 'about'})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class MakePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/make_post.html'
    context_object_name = 'form'
    form_class = MakePostForm


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('blog-home')
