from django.db import migrations


def add_appliance_installations_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    slug = "appliance-installations"

    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            "title": "Appliance Installations",
            "subtitle": "Safe, code‑compliant installs for major appliances and specialized equipment.",
            "intro_heading": "Safe and Professional Appliance Installations in Maine",
            "intro_body": (
                "When it comes to installing major appliances, proper electrical connections are critical to safety "
                "and performance. At ACS Electrical Contractors, we provide professional appliance installation services for homes, "
                "rental units, and businesses across Maine. Whether you're replacing a kitchen appliance, upgrading "
                "laundry equipment, or adding a new hardwired unit, our licensed electricians ensure everything is "
                "wired correctly, securely, and to code."
            ),
            "why_heading": "Why Trust ACS Electrical Contractors for Appliance Installations?",
            "why_body": (
                "Many appliances require more than just plugging them in — they need dedicated circuits, proper "
                "grounding, and sometimes hardwiring. Our team will inspect your existing setup, make any necessary "
                "electrical upgrades, and install your appliance safely and efficiently. We handle everything from "
                "ovens and dryers to dishwashers and electric ranges — with no shortcuts."
            ),
            "image": "img/appliance-installations.png",
        },
    )

    if not created:
        service.title = "Appliance Installations"
        service.intro_heading = "Safe and Professional Appliance Installations in Maine"
        service.intro_body = (
            "When it comes to installing major appliances, proper electrical connections are critical to safety "
            "and performance. At ACS Electrical Contractors, we provide professional appliance installation services for homes, "
            "rental units, and businesses across Maine. Whether you're replacing a kitchen appliance, upgrading "
            "laundry equipment, or adding a new hardwired unit, our licensed electricians ensure everything is "
            "wired correctly, securely, and to code."
        )
        service.why_heading = "Why Trust ACS Electrical Contractors for Appliance Installations?"
        service.why_body = (
            "Many appliances require more than just plugging them in — they need dedicated circuits, proper "
            "grounding, and sometimes hardwiring. Our team will inspect your existing setup, make any necessary "
            "electrical upgrades, and install your appliance safely and efficiently. We handle everything from "
            "ovens and dryers to dishwashers and electric ranges — with no shortcuts."
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
            "title": "Code-Compliant Wiring",
            "text": "Avoid safety hazards and meet all local and national electrical standards.",
        },
        {
            "title": "Hassle-Free Setup",
            "text": "We handle the electrical connections so your appliance is ready to use immediately.",
        },
        {
            "title": "Upgrades as Needed",
            "text": "We’ll install new outlets, breakers, or circuits if your current system can’t support the load.",
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
            "question": "What types of appliances do you install?",
            "answer": (
                "We install electric ranges, ovens, dishwashers, microwaves, dryers, water heaters, air conditioners, "
                "and more — anything that requires electrical expertise."
            ),
        },
        {
            "question": "Can you install appliances in rental properties or condos?",
            "answer": (
                "Yes. We regularly work with landlords and property managers to install or upgrade appliances in "
                "apartments, condos, and multi-unit dwellings."
            ),
        },
        {
            "question": "Do I need a dedicated circuit for my appliance?",
            "answer": (
                "Many appliances — especially dryers, ovens, and dishwashers — require dedicated circuits. If your "
                "panel is full or outdated, we can upgrade it to support the load safely."
            ),
        },
    ]
    existing_faqs = set(
        FAQ.objects.filter(service=service).values_list("question", flat=True)
    )
    for f in faqs:
        if f["question"] not in existing_faqs:
            FAQ.objects.create(
                service=service, question=f["question"], answer=f["answer"]
            )


def remove_appliance_installations_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    service = Service.objects.filter(slug="appliance-installations").first()
    if service:
        service.delete()


class Migration(migrations.Migration):

    dependencies = [
        # 🔁 Replace with your latest migration in the "core" app
        ("core", "0006_auto_20250906_1517"),
    ]

    operations = [
        migrations.RunPython(
            add_appliance_installations_service,
            remove_appliance_installations_service,
        ),
    ]
