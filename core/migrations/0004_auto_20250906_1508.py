from django.db import migrations


def add_solar_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    slug = "solar-electrical-systems"

    # Upsert the Service
    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            "title": "Solar Electrical Systems",
            "subtitle": "On‑grid or off‑grid designs customized to your property and goals.",
            "intro_heading": "Solar Electrical Systems — On-Grid and Off-Grid Solutions in Maine",
            "intro_body": (
                "ACS Maine designs and installs safe, reliable solar electrical systems for homes, camps, and "
                "businesses throughout Maine. Whether you're looking to reduce your electric bill with a grid-tied "
                "system or power a remote cabin completely off-grid, we provide expert solar wiring and integration "
                "services. Our team ensures your solar setup is not only efficient, but also fully code-compliant and "
                "built to withstand Maine’s climate."
            ),
            "why_heading": "Why Choose ACS Maine for Solar Electrical Work?",
            "why_body": (
                "Solar power is a smart investment — but only when it's installed right. ACS Maine brings deep "
                "experience in wiring solar systems for both utility-connected and independent applications. We handle "
                "everything from panel connections and inverters to battery storage and system integration. Our focus "
                "is on safety, system longevity, and making sure you get the most out of your solar investment."
            ),
            "image": "img/solar-electrical-systems.png",
        },
    )

    # If it already exists, refresh core fields (idempotent behavior)
    if not created:
        service.title = "Solar Electrical Systems"
        service.intro_heading = (
            "Solar Electrical Systems — On-Grid and Off-Grid Solutions in Maine"
        )
        service.intro_body = (
            "ACS Maine designs and installs safe, reliable solar electrical systems for homes, camps, and "
            "businesses throughout Maine. Whether you're looking to reduce your electric bill with a grid-tied "
            "system or power a remote cabin completely off-grid, we provide expert solar wiring and integration "
            "services. Our team ensures your solar setup is not only efficient, but also fully code-compliant and "
            "built to withstand Maine’s climate."
        )
        service.why_heading = "Why Choose ACS Maine for Solar Electrical Work?"
        service.why_body = (
            "Solar power is a smart investment — but only when it's installed right. ACS Maine brings deep "
            "experience in wiring solar systems for both utility-connected and independent applications. We handle "
            "everything from panel connections and inverters to battery storage and system integration. Our focus "
            "is on safety, system longevity, and making sure you get the most out of your solar investment."
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
            "title": "Custom-Designed Systems",
            "text": "We tailor every solar project to your property, power needs, and future goals.",
        },
        {
            "title": "Off-Grid Expertise",
            "text": "Need power in a remote location? We specialize in stand-alone systems with battery storage.",
        },
        {
            "title": "Code-Ready & Inspected",
            "text": "We wire to NEC standards and coordinate inspections and utility approvals when needed.",
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
            "question": "Do you install the solar panels too, or just the wiring?",
            "answer": (
                "We focus on the electrical side — wiring, inverters, grounding, disconnects, and integration. "
                "If you’re working with a solar supplier or installer, we’ll partner with them to ensure the system "
                "is connected safely and properly."
            ),
        },
        {
            "question": "What’s the difference between on-grid and off-grid systems?",
            "answer": (
                "On-grid systems are connected to the utility and can send excess power back to the grid. "
                "Off-grid systems operate independently with battery storage and are ideal for remote properties "
                "without utility access."
            ),
        },
        {
            "question": "Can I use solar to power my whole home or camp?",
            "answer": (
                "Yes — with proper design and energy management. We’ll assess your usage and help plan a system "
                "that meets your needs, whether it’s full power or critical-load coverage."
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


def remove_solar_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    service = Service.objects.filter(slug="solar-electrical-systems").first()
    if service:
        service.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_auto_20250906_1505"),
    ]

    operations = [
        migrations.RunPython(add_solar_service, remove_solar_service),
    ]
