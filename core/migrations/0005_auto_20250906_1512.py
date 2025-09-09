from django.db import migrations


def add_lighting_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    slug = "interior-exterior-building-lighting"

    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            "title": "Interior & Exterior Building Lighting",
            "subtitle": "Brighten and secure your property with efficient, long‑lasting lighting solutions.",
            "intro_heading": "Interior and Exterior Lighting Installation in Maine",
            "intro_body": (
                "At ACS Electrical Contractors, we offer professional interior and exterior building lighting "
                "installation for residential, commercial, and industrial properties. Whether you’re looking to "
                "brighten up a living space, improve outdoor security, or highlight architectural features, our "
                "licensed electricians deliver lighting solutions that are efficient, attractive, and built to last. "
                "We’ll help you choose the right fixtures, plan the layout, and wire everything safely — indoors and out."
            ),
            "why_heading": "Why Choose ACS for Your Lighting Project?",
            "why_body": (
                "Lighting does more than illuminate — it enhances safety, improves productivity, and brings out the "
                "best in your property. Our team designs and installs custom lighting systems tailored to your needs, "
                "whether it’s functional lighting for workspaces, ambient lighting for living areas, or security "
                "lighting for driveways and entrances. With ACS Maine, your lighting is thoughtfully planned, "
                "professionally installed, and future-ready."
            ),
            "image": "img/interior-exterior-building-lighting.png",
        },
    )

    if not created:
        service.title = "Interior & Exterior Building Lighting"
        service.intro_heading = "Interior and Exterior Lighting Installation in Maine"
        service.intro_body = (
            "At ACS Electrical Contractors, we offer professional interior and exterior building lighting "
            "installation for residential, commercial, and industrial properties. Whether you’re looking to "
            "brighten up a living space, improve outdoor security, or highlight architectural features, our "
            "licensed electricians deliver lighting solutions that are efficient, attractive, and built to last. "
            "We’ll help you choose the right fixtures, plan the layout, and wire everything safely — indoors and out."
        )
        service.why_heading = "Why Choose ACS for Your Lighting Project?"
        service.why_body = (
            "Lighting does more than illuminate — it enhances safety, improves productivity, and brings out the "
            "best in your property. Our team designs and installs custom lighting systems tailored to your needs, "
            "whether it’s functional lighting for workspaces, ambient lighting for living areas, or security "
            "lighting for driveways and entrances. With ACS Maine, your lighting is thoughtfully planned, "
            "professionally installed, and future-ready."
        )
        service.save(
            update_fields=[
                "title",
                "intro_heading",
                "intro_body",
                "why_heading",
                "why_body",
            ]
        )

    # Bullet points (dedupe by title)
    bullets = [
        {
            "title": "Improved Safety & Security",
            "text": "Outdoor lighting helps deter crime and reduce tripping hazards at night.",
        },
        {
            "title": "Custom Interior Ambiance",
            "text": "We install lighting that’s matched to the mood and function of each room.",
        },
        {
            "title": "Energy Efficiency",
            "text": "Upgrade to LED systems and smart controls that reduce energy usage and long-term costs.",
        },
    ]
    existing_bullets = set(
        BulletPoint.objects.filter(service=service).values_list("title", flat=True)
    )
    for b in bullets:
        if b["title"] not in existing_bullets:
            BulletPoint.objects.create(
                service=service, title=b["title"], text=b["text"]
            )

    # FAQs (dedupe by question)
    faqs = [
        {
            "question": "Can you install both new and replacement lighting?",
            "answer": (
                "Yes — we install brand new lighting systems for new construction, as well as retrofit existing "
                "spaces with upgraded fixtures or wiring."
            ),
        },
        {
            "question": "Do you install motion sensors, dimmers, and timers?",
            "answer": (
                "Absolutely. We offer smart lighting solutions including motion detection, programmable timers, and "
                "dimmable switches for convenience and energy savings."
            ),
        },
        {
            "question": "What types of outdoor lighting do you install?",
            "answer": (
                "We install pathway lights, security lights, wall-mounted fixtures, floodlights, soffit lighting, and "
                "more — all designed to stand up to Maine weather and maximize visibility."
            ),
        },
    ]
    existing_questions = set(
        FAQ.objects.filter(service=service).values_list("question", flat=True)
    )
    for f in faqs:
        if f["question"] not in existing_questions:
            FAQ.objects.create(
                service=service, question=f["question"], answer=f["answer"]
            )


def remove_lighting_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    service = Service.objects.filter(slug="interior-exterior-building-lighting").first()
    if service:
        service.delete()


class Migration(migrations.Migration):

    dependencies = [
        # 🔁 Replace with your latest migration in the "core" app
        ("core", "0004_auto_20250906_1508"),
    ]

    operations = [
        migrations.RunPython(add_lighting_service, remove_lighting_service),
    ]
