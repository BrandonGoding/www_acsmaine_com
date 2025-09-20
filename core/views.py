from django.views.generic import TemplateView, DetailView, ListView
from .models import Service
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm


class AboutView(TemplateView):
    template_name = "core/about_acs_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()

        features = [
            {
                "title": "Experience",
                "text": "Our certified electricians bring years of expertise to every project.",
            },
            {
                "title": "Versatility",
                "text": "From residential upgrades to commercial & industrial systems—we’ve got you covered.",
            },
            {
                "title": "Local Expertise",
                "text": "We understand local codes and tailor solutions for our community.",
            },
            {
                "title": "Safety First",
                "text": "We adhere to top industry standards to ensure your safety.",
            },
            {
                "title": "Customer-Centric",
                "text": "Collaborative and transparent—we work within your needs and budget.",
            },
            {
                "title": "Reliability",
                "text": "Trusted for over two decades as your go-to electrical partner.",
            },
        ]
        context["features"] = features

        return context
