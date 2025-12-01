from django.contrib import admin
from core.models import Service, BulletPoint, FAQ


class BulletPointInline(admin.TabularInline):
    model = BulletPoint
    extra = 1           # how many empty rows to show
    fields = ("title", "text")
    # If you want to make text a bit more compact, you can exclude it and use raw_id_fields, etc.


class FAQInline(admin.StackedInline):
    model = FAQ
    extra = 1
    fields = ("question", "answer")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "slug")
    search_fields = ("title", "subtitle", "intro_heading", "why_heading")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [BulletPointInline, FAQInline]

    # Optional: organize the form nicely
    fieldsets = (
        (None, {
            "fields": ("title", "subtitle", "slug", "image"),
        }),
        ("Intro Section", {
            "fields": ("intro_heading", "intro_body"),
        }),
        ("Why Section", {
            "fields": ("why_heading", "why_body"),
        }),
    )
