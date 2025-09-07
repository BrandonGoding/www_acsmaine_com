from django.views.generic import TemplateView, DetailView, ListView
from .models import Service


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()

        features = [
            {"title": "Experience", "text": "Our certified electricians bring years of expertise to every project."},
            {"title": "Versatility",
             "text": "From residential upgrades to commercial & industrial systems—we’ve got you covered."},
            {"title": "Local Expertise", "text": "We understand local codes and tailor solutions for our community."},
            {"title": "Safety First", "text": "We adhere to top industry standards to ensure your safety."},
            {"title": "Customer-Centric",
             "text": "Collaborative and transparent—we work within your needs and budget."},
            {"title": "Reliability", "text": "Trusted for over two decades as your go-to electrical partner."},
        ]
        context['features'] = features

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
        context['services'] = Service.objects.filter().exclude(id=self.object.id)
        return context
