from django.views.generic import TemplateView, DetailView
from .models import Service


class HomeView(TemplateView):
    template_name = "core/home.html"


class ServiceDetailView(DetailView):
    template_name = "core/services/detail.html"
    model = Service
