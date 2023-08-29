from django.views.generic import TemplateView, DetailView, ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import BlogPost, Contact

class HomeView(ListView):
    model = BlogPost
    fields = '__all__'
    context_object_name = 'blogs'
    template_name = "home.html"

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'description')
    success_url = reverse_lazy('blog')
    template_name = "blog_create.html"
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog')
    template_name = "blog_delete.html"

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'description')
    success_url = reverse_lazy('blog')
    template_name = "blog_update.html"



class BlogListView(ListView):
    model = BlogPost
    context_object_name = 'blogs'
    template_name = "blog.html"


class BlogSearchView(ListView):
    model = BlogPost
    context_object_name = 'blogs'
    template_name = "blog_search.html"

    def get_queryset(self):
        query = self.request.GET.get('title')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list
    
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"


class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    success_url = '200'
    template_name = "contact.html"

class Contact200View(TemplateView):
    template_name = "contact_ok.html"
