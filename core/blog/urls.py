from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from . import views

app_name = "blog"

urlpatterns = [
    #path('cbv-index', views.IndexView.as_view(), name="cbv-index"),
    #path("go-to-maktab/<int:pk>", views.Redirecttoitmeter.as_view(), name="go-to-maktab"),
    path('post/', views.PostListView.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/create/', views.PostCreateView.as_view(), name="post-create"),


]