"""
URL configuration for acsmaine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from core import views as website_views
from django.http import HttpResponse
from django.urls import path


def robots_txt(request):
    content = "User-agent: *\nDisallow: /"
    return HttpResponse(content, content_type="text/plain")


urlpatterns = [
    path("robots.txt", robots_txt, name="robots_txt"),
    path("", website_views.HomeView.as_view(), name="home"),
    path("about/", website_views.AboutView.as_view(), name="about"),
    path("contact/", website_views.contact, name="contact"),
    path("services/", website_views.ServiceListView.as_view(), name="services_list"),
    path(
        "services/<slug:slug>/",
        website_views.ServiceDetailView.as_view(),
        name="services_detail",
    ),
    path("payments/", website_views.payments, name="payments"),
    path("admin/", admin.site.urls),
]
