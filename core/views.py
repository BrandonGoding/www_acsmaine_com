from django.views.generic import TemplateView, DetailView, ListView
from .models import Service
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm


from django.conf import settings
from django.core.mail import send_mail


def send_service_request_email(cleaned_data):
    """
    Send an email to you (and optionally a confirmation to the customer)
    when a new service request is submitted.
    """
    # Extract fields safely from the form
    name = cleaned_data.get("name")
    service_address = cleaned_data.get("service_address")
    phone = cleaned_data.get("phone")
    email = cleaned_data.get("email")  # could be a FK or choice field
    work_desired = cleaned_data.get("work_desired")

    subject = f"New service request from {name or 'Unknown'}"
    recipient_list = [settings.CONTACT_EMAIL]  # set this in your settings.py
    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None)

    body = (
        f"New service request:\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Service Address: {service_address}\n\n"
        f"Work Desired:\n{work_desired}\n"
    )

    send_mail(
        subject=subject,
        message=body,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )

    # Optional: send a confirmation email back to the user
    if email:
        send_mail(
            subject="We received your service request",
            message=(
                f"Hi {name or ''},\n\n"
                "Thanks for reaching out! We’ve received your request and will "
                "be in touch shortly.\n\n"
                "— ACS Electrical Contractors"
            ),
            from_email=from_email,
            recipient_list=[email],
            fail_silently=True,
        )



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
            send_service_request_email(form.cleaned_data)
            messages.success(request, "Thanks for submitting! We’ll be in touch shortly.")
            return redirect("contact")  # PRG pattern
        else:
            messages.error(request, "Please fix the errors below and resubmit.")
    else:
        form = ServiceRequestForm()

    return render(request, "core/contact.html", {"form": form, "services": Service.objects.all()})


def payments(request):
    context = {'services': Service.objects.all()}
    return render(request, "core/payments.html", context=context)