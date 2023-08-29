from django.views.generic import (
    TemplateView,
    DetailView, 
    ListView, 
    CreateView, 
    DeleteView, 
    UpdateView
    )
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse_lazy, reverse

from .models import BlogPost, Contact

class HomeView(ListView):
    model = BlogPost
    fields = '__all__'
    context_object_name = 'blogs'
    template_name = "home.html"

class BlogCreateView(LoginRequiredMixin ,CreateView):
    model = BlogPost
    fields = ('title', 'description')
    success_url = reverse_lazy('blog')
    login_url='login'
    template_name = "blog_create.html"
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class BlogDeleteView(LoginRequiredMixin ,DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog')
    login_url='login'
    template_name = "blog_delete.html"

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ('title', 'description')
    success_url = reverse_lazy('blog')
    login_url='login'
    template_name = "blog_update.html"



class BlogListView(LoginRequiredMixin, ListView):
    model = BlogPost
    context_object_name = 'blogs'
    login_url='login'
    template_name = "blog.html"


class BlogSearchView(LoginRequiredMixin, ListView):
    model = BlogPost
    context_object_name = 'blogs'
    login_url='login'
    template_name = "blog_search.html"

    def get_queryset(self):
        query = self.request.GET.get('title')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list
    
class BlogDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    login_url='login'
    template_name = "blog_detail.html"


class AboutView(TemplateView):
    template_name = "about.html"

class Contact200View(TemplateView):
    template_name = "contact_ok.html"

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    success_url = '200'
    template_name = "contact.html"

