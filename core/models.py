from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page, Orderable


class HomePage(Page):
    max_count = 1
    subpage_types = [
        'core.AboutACSPage',
        'core.ServiceListingPage',
    ]


class AboutACSPage(Page):
    max_count = 1
    subpage_types = []

    content_panels = Page.content_panels + [
        InlinePanel("features", label="Features"),
    ]


class ContactACSPage(Page):
    max_count = 1
    subpage_types = []


class PaymentPage(Page):
    max_count = 1
    subpage_types = []


class FeatureItem(Orderable):
    page = ParentalKey(AboutACSPage, related_name="features", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    panels = [
        FieldPanel("title"),
        FieldPanel("text"),
    ]


class ServiceListingPage(Page):
    max_count = 1
    subpage_types = [
        'core.ServicePage',
    ]


class ServicePage(Page):
    subpage_types = []
    subtitle = models.CharField(max_length=255)
    intro_heading = models.CharField(max_length=255)
    intro_body = models.TextField()
    why_heading = models.CharField(max_length=255)
    why_body = models.TextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Service image",
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('intro_heading'),
        FieldPanel('intro_body'),
        FieldPanel('why_heading'),
        FieldPanel('why_body'),
        InlinePanel("bullet_points", label="Bullet Points"),
        InlinePanel("faqs", label="FAQs"),
    ]

class BulletPointItem(Orderable):
    page = ParentalKey(ServicePage, related_name="bullet_points", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    panels = [
        FieldPanel("title"),
        FieldPanel("text"),
    ]

class FrequentlyAskedQuestion(Orderable):
    page = ParentalKey(ServicePage, related_name="faqs", on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.TextField()

    panels = [
        FieldPanel("question"),
        FieldPanel("answer"),
    ]


class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    intro_heading = models.CharField(max_length=200)
    intro_body = models.TextField()
    why_heading = models.CharField(max_length=200)
    why_body = models.TextField()
    image = models.ImageField(upload_to="services/", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class BulletPoint(models.Model):
    service = models.ForeignKey(
        Service, related_name="bullet_points", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField()


class FAQ(models.Model):
    service = models.ForeignKey(Service, related_name="faqs", on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.TextField()
