from django.urls import path
from .views import (
    HomePageView, 
    AboutPageView,
    BlogPageView,
    JupiterPageView
    )


urlpatterns = [
    path('about/', AboutPageView.as_view(),name='about'),
    path('blog/', BlogPageView.as_view(),name='blog'),
    path('jupiter/', JupiterPageView.as_view(),name='jupiter'),
    path('', HomePageView.as_view(), name='home'),
    ]