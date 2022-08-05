from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   # Added for UpdateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView   # UpdateView added
from .models import Review


def home(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews/home.html', context)


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/home.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']


class ReviewDetailView(DetailView):
    model = Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['artist', 'album', 'image', 'rating', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Added for UpdateView
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['rating', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True 
        return False


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False


def about(request):
    return render(request, 'reviews/about.html', {'title': 'About'})