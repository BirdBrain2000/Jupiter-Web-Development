from django.urls import path

from .views import HomePageView, BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/post/new/', BlogCreateView.as_view(), name='post_new'),
    path('blog/post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('blog/', BlogListView.as_view(), name='blog'),
    ]