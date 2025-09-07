from django.views.generic import TemplateView, DetailView, ListView
from .models import Service
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm


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


def contact(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            # TODO: send email / save to DB / create ticket
            messages.success(request, "Thanks for submitting! We’ll be in touch shortly.")
            return redirect("contact")  # PRG pattern
        else:
            messages.error(request, "Please fix the errors below and resubmit.")
    else:
        form = ServiceRequestForm()

    return render(request, "core/contact.html", {"form": form})
