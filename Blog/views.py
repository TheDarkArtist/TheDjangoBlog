from django.views.generic import TemplateView, DetailView, ListView

from .models import BlogPost

class HomeView(TemplateView):
    template_name = "home.html"

class BlogListView(ListView):
    model = BlogPost
    context_object_name = 'blogs'
    template_name = "blog.html"


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"


class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"
