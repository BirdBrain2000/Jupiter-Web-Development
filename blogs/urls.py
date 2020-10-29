from django.urls import path

from .views import (
    HomePageView, 
    BlogListView, 
    BlogDetailView, 
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    JupiterPageView,
    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('blog/post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('blog/post/new/', BlogCreateView.as_view(), name='post_new'),
    path('blog/post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('jupiter/', JupiterPageView.as_view(), name='jupiter'),
    ]