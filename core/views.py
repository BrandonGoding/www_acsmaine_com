from django.views.generic import TemplateView, DetailView, ListView
from .models import Service


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class ServiceListView(ListView):
    template_name = "core/services/list.html"
    model = Service
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    template_name = "core/services/detail.html"
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context
