from django.db import migrations


def add_generators_transfer_switch_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    slug = "generators-transfer-switch-installation"

    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            "title": "Generators & Transfer Switch Installation",
            "subtitle": "Professional generator and transfer switch installation for dependable backup power.",
            "intro_heading": "Generator and Transfer Switch Installation in Maine",
            "intro_body": (
                "Power outages in Maine can happen any time of year — from summer storms to winter ice. "
                "At ACS Electrical Contractors, we offer professional generator and transfer switch installation "
                "to keep your home or business running no matter the weather. Whether you're installing a portable "
                "generator hookup or a fully automated standby system, we ensure your setup is safe, seamless, and "
                "built to keep the lights (and heat) on when it matters most."
            ),
            "why_heading": "Why Install a Generator with ACS?",
            "why_body": (
                "Installing a generator isn’t just about convenience — it’s about safety, comfort, and business "
                "continuity. Our licensed electricians will help you choose the right size and type of generator, "
                "install the proper wiring and transfer switch, and ensure your system is ready when the power goes "
                "out. We provide clean, code-compliant installations that protect your property and your peace of mind."
            ),
            "image": "img/generator-and-transfer-switch-installs.png",
        },
    )

    # keep fields fresh if it already exists (idempotent upsert)
    if not created:
        service.title = "Generators & Transfer Switch Installation"
        service.intro_heading = "Generator and Transfer Switch Installation in Maine"
        service.intro_body = (
            "Power outages in Maine can happen any time of year — from summer storms to winter ice. "
            "At ACS Electrical Contractors, we offer professional generator and transfer switch installation "
            "to keep your home or business running no matter the weather. Whether you're installing a portable "
            "generator hookup or a fully automated standby system, we ensure your setup is safe, seamless, and "
            "built to keep the lights (and heat) on when it matters most."
        )
        service.why_heading = "Why Install a Generator with ACS?"
        service.why_body = (
            "Installing a generator isn’t just about convenience — it’s about safety, comfort, and business "
            "continuity. Our licensed electricians will help you choose the right size and type of generator, "
            "install the proper wiring and transfer switch, and ensure your system is ready when the power goes "
            "out. We provide clean, code-compliant installations that protect your property and your peace of mind."
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
            "title": "Automatic Backup Power",
            "text": "Standby systems detect outages and turn on automatically — no fumbling in the dark.",
        },
        {
            "title": "Safe & Code-Compliant Installation",
            "text": "Proper grounding, transfer switches, and interlocks keep your family or staff safe.",
        },
        {
            "title": "Customized to Your Needs",
            "text": "We size systems to match your home or business — no more, no less.",
        },
    ]
    existing_titles = set(
        BulletPoint.objects.filter(service=service).values_list("title", flat=True)
    )
    for b in bullets:
        if b["title"] not in existing_titles:
            BulletPoint.objects.create(
                service=service, title=b["title"], text=b["text"]
            )

    # FAQs (dedupe by question)
    faqs = [
        {
            "question": "What’s the difference between a manual and automatic transfer switch?",
            "answer": (
                "A manual transfer switch requires you to physically switch power to the generator during an outage. "
                "An automatic transfer switch does this for you instantly and safely — ideal for whole-home or commercial systems."
            ),
        },
        {
            "question": "Do I need a permit to install a generator or switch?",
            "answer": (
                "Yes, but don’t worry — ACS Electrical Contractors handles all required permits and inspections to ensure your system meets code."
            ),
        },
        {
            "question": "What size generator do I need?",
            "answer": (
                "That depends on what you want to power during an outage. We’ll walk you through your options and "
                "calculate the correct size based on your essential loads."
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


def remove_generators_transfer_switch_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    svc = Service.objects.filter(slug="generators-transfer-switch-installation").first()
    if svc:
        svc.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_auto_20250906_1526"),
    ]

    operations = [
        migrations.RunPython(
            add_generators_transfer_switch_service,
            remove_generators_transfer_switch_service,
        ),
    ]
