from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Utensils
from django.urls import reverse_lazy

class HomePageView(ListView):
    template_name = 'home.html'
    model = Utensils
    context_object_name = 'utensils'

class UtensilsDetailView(DetailView):
    template_name = 'detail.html'
    model = Utensils

class UtensilsCreateView(CreateView):
    model = Utensils
    template_name = 'create.html'
    fields = ['title', 'author', 'description', 'img']

class UtensilsUpdateView(UpdateView):
    model = Utensils
    template_name = 'update.html'
    fields = ['title', 'description', 'img']

class DeleteUpdateView(DeleteView):
    model = Utensils
    template_name = 'delete.html'
    success_url = reverse_lazy('home')