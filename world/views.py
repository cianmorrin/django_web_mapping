from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import WorldBorder, Post, Flight
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin  # this is needed for class views, can't use login required
from world.quotes import get_quote


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
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'dream_holiday', 'reason']
    success_url = '/'

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
def flights(request):
    quotes = []
    prettystring = ''
    if request.method == 'POST':
        loc_from_arr = request.POST.get('airportorigin')
        print(loc_from_arr)
        if loc_from_arr is None:
            loc_from = ""
        else:
            loc_from = loc_from_arr.split(",")
            loc_from = loc_from[0]

        loc_to_arr = request.POST.get('airportdestination')
        print(loc_to_arr)
        if loc_to_arr is None:
            loc_to = ""
        else:
            loc_to = loc_to_arr.split(",")
            loc_to = loc_to[0]

        date = request.POST.get('date')
        prettystring, quotes = get_quote(loc_from, loc_to, date)
        if len(quotes) == 0:
            quotes.append('No flights for your choice')
    context = {
        'airports': Flight.objects.all(),
        'quotes': quotes,
        'prettystring': prettystring,
    }
    return render(request, 'world/flights.html', context)
