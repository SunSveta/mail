from django.urls import path

from blog.apps import BlogConfig
from blog.views import *


app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]