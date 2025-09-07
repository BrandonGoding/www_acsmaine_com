from django.db import migrations


def add_electric_heat_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    slug = "electric-heat-installations"

    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            "title": "Electric Heat Installations",
            "subtitle": "Energy‑efficient electric heating systems for comfort and cost savings.",
            "intro_heading": "Professional Electric Heat Installation in Maine",
            "intro_body": (
                "At ACS Electrical Contractors, we provide reliable, energy-efficient electric heat installation for "
                "homes, apartments, and commercial spaces across Maine. Whether you're upgrading from an outdated system "
                "or building new, our licensed electricians install safe, effective electric heating solutions tailored "
                "to your building and climate needs. From baseboard units to wall heaters and thermostats, we ensure "
                "everything is installed to code and ready to keep you warm through the harshest Maine winters."
            ),
            "why_heading": "Why Choose ACS for Electric Heat Installation?",
            "why_body": (
                "Electric heating systems offer quiet operation, easy zone control, and consistent warmth — without the "
                "need for fuel deliveries or ductwork. At ACS, we help you choose the best heating option for your space, "
                "install it properly, and wire it for safety and performance. You get a heating solution that’s "
                "low-maintenance, affordable, and built to last."
            ),
            "image": 'img/electrical-heat-installations.png',
        },
    )

    # keep fields fresh if already present (idempotent behavior)
    if not created:
        service.title = "Electric Heat Installations"
        service.intro_heading = "Professional Electric Heat Installation in Maine"
        service.intro_body = (
            "At ACS Electrical Contractors, we provide reliable, energy-efficient electric heat installation for "
            "homes, apartments, and commercial spaces across Maine. Whether you're upgrading from an outdated system "
            "or building new, our licensed electricians install safe, effective electric heating solutions tailored "
            "to your building and climate needs. From baseboard units to wall heaters and thermostats, we ensure "
            "everything is installed to code and ready to keep you warm through the harshest Maine winters."
        )
        service.why_heading = "Why Choose ACS for Electric Heat Installation?"
        service.why_body = (
            "Electric heating systems offer quiet operation, easy zone control, and consistent warmth — without the "
            "need for fuel deliveries or ductwork. At ACS, we help you choose the best heating option for your space, "
            "install it properly, and wire it for safety and performance. You get a heating solution that’s "
            "low-maintenance, affordable, and built to last."
        )
        service.save(update_fields=["title", "intro_heading", "intro_body", "why_heading", "why_body"])

    # Bullet points (dedupe by title)
    bullets = [
        {"title": "Energy-Efficient Comfort", "text": "Electric heat converts nearly all energy to warmth with minimal waste."},
        {"title": "Flexible Installation", "text": "Ideal for remodels, additions, and areas where traditional heating isn't practical."},
        {"title": "Safe and Low-Maintenance", "text": "No combustion, no venting, and minimal upkeep required."},
    ]
    existing_bullets = set(BulletPoint.objects.filter(service=service).values_list("title", flat=True))
    for b in bullets:
        if b["title"] not in existing_bullets:
            BulletPoint.objects.create(service=service, title=b["title"], text=b["text"])

    # FAQs (dedupe by question)
    faqs = [
        {
            "question": "What types of electric heat systems do you install?",
            "answer": (
                "We install electric baseboard heaters, wall-mounted panel heaters, in-floor radiant systems, and "
                "programmable thermostats — all matched to your space and usage."
            ),
        },
        {
            "question": "Is electric heat expensive to run?",
            "answer": (
                "Electric heat is very efficient at the point of use, and modern systems with thermostats and zoning can "
                "keep costs down. It's a great option for supplemental or whole-home heating, especially in well-insulated buildings."
            ),
        },
        {
            "question": "Can you add electric heat during a renovation?",
            "answer": (
                "Absolutely. Electric heating is ideal for renovations or additions where ductwork or fuel lines aren’t "
                "feasible. We’ll design a system that integrates cleanly with your new space."
            ),
        },
    ]
    existing_faqs = set(FAQ.objects.filter(service=service).values_list("question", flat=True))
    for f in faqs:
        if f["question"] not in existing_faqs:
            FAQ.objects.create(service=service, question=f["question"], answer=f["answer"])


def remove_electric_heat_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    svc = Service.objects.filter(slug="electric-heat-installations").first()
    if svc:
        svc.delete()


class Migration(migrations.Migration):

    dependencies = [
        # 🔁 Replace with your latest migration in the "core" app
        ("core", "0008_auto_20250906_1523"),
    ]

    operations = [
        migrations.RunPython(add_electric_heat_service, remove_electric_heat_service),
    ]
