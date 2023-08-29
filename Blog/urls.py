from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<pk>/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<pk>', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/<pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/search/', views.BlogSearchView.as_view(), name='blog_search'),
    
]
