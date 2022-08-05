from django.urls import path
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView   # Added for UpdateView
from . import views


urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews-home'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/new/', ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),   # Added for UpdateView
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('about/', views.about, name='reviews-about'),
]