from django.urls import path

from .views import HomePageView, BlogListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog'),
    ]