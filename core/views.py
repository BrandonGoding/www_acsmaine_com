from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = "core/home.html"

def service_pools_saunas(request):
    bullets = [
        {"title": "Code-Compliant & Inspected", "text": "We ensure your setup meets NEC and Maine electrical safety standards."},
        {"title": "Peace of Mind Around Water", "text": "GFCI protection and proper grounding keep your family and guests safe."},
        {"title": "Complete Integration", "text": "We handle pumps, heaters, lights, timers, and control systems — wired right the first time."},
    ]

    faqs = [
        {"q": "Do I need a dedicated circuit for my hot tub or pool?", "a": "Yes. Dedicated circuits + GFCI + bonding are typically required."},
        {"q": "Can you wire both indoor and outdoor spa features?", "a": "Absolutely. We protect wiring from moisture, corrosion, and weather."},
        {"q": "How soon can you install?", "a": "We coordinate with your delivery/installer for a fast, clean install."},
    ]

    return render(request, "core/services/detail.html", {
        "title": "Sauna, Pool & Jacuzzi Electrical Work",
        "intro_heading": "Sauna, Pool, and Jacuzzi Electrical Installation in Maine",
        "intro_body": "ACS Maine provides specialized electrical services for saunas, pools, hot tubs, and Jacuzzis...",
        "why_heading": "Why Trust ACS for Your Spa & Pool Electrical Work?",
        "why_body": "Working with water and electricity demands experience, attention to detail, and a deep understanding of safety codes...",
        "bullets": bullets,
        "faqs": faqs,
    })
