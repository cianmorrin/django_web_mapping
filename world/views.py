from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import WorldBorder, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # this is needed for class views, can't use login required


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'world/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'world/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'dream_holiday', 'reason']
    # add success url and redirect to home page

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'dream_holiday', 'reason']
    # add success url and redirect to home page

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # this tests if the user is the author of the post that is currently trying to be updated
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def friends(request):
    context = {
        'countries': WorldBorder.objects.all()
    }
    return render(request, 'world/countries.html', context)


