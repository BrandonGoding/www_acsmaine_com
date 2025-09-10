from django.db import models


# Create your models here.
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
