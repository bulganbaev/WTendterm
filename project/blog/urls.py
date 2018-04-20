from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.BlogListView.as_view(), name='home'),
    url('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
]