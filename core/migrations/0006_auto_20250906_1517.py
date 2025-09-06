from django.db import migrations


def add_knob_and_tube_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    slug = "knob-and-tube-wiring-replacement"

    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            "title": "Knob and Tube Wiring Replacement",
            "intro_heading": "Knob and Tube Wiring Replacement Services in Maine",
            "intro_body": (
                "At ACS Electrical Contractors, we provide expert knob and tube wiring replacement to help homeowners "
                "and property owners bring their electrical systems up to modern safety and efficiency standards. "
                "Knob and tube wiring, common in homes built before the 1950s, poses significant fire risks and is "
                "often unable to handle the electrical demands of today’s appliances and devices. Our licensed "
                "electricians will carefully remove outdated wiring and install safe, code-compliant systems that "
                "protect your property and your family."
            ),
            "why_heading": "Why Replace Knob and Tube Wiring with ACS?",
            "why_body": (
                "Replacing knob and tube wiring is one of the most important upgrades you can make to an older home. "
                "ACS has the experience and expertise to handle these delicate projects with minimal disruption, "
                "ensuring your home is safer, your insurance coverage is secure, and your electrical system is ready "
                "for modern life."
            ),
            "image": "img/knob-and-tube-wiring-replacement.png",
        },
    )

    # If already existed, refresh the main fields for idempotency
    if not created:
        service.title = "Knob and Tube Wiring Replacement"
        service.intro_heading = "Knob and Tube Wiring Replacement Services in Maine"
        service.intro_body = (
            "At ACS Electrical Contractors, we provide expert knob and tube wiring replacement to help homeowners "
            "and property owners bring their electrical systems up to modern safety and efficiency standards. "
            "Knob and tube wiring, common in homes built before the 1950s, poses significant fire risks and is "
            "often unable to handle the electrical demands of today’s appliances and devices. Our licensed "
            "electricians will carefully remove outdated wiring and install safe, code-compliant systems that "
            "protect your property and your family."
        )
        service.why_heading = "Why Replace Knob and Tube Wiring with ACS?"
        service.why_body = (
            "Replacing knob and tube wiring is one of the most important upgrades you can make to an older home. "
            "ACS has the experience and expertise to handle these delicate projects with minimal disruption, "
            "ensuring your home is safer, your insurance coverage is secure, and your electrical system is ready "
            "for modern life."
        )
        service.save(update_fields=["title", "intro_heading", "intro_body", "why_heading", "why_body"])

    # Bullet points (dedupe by title)
    bullets = [
        {
            "title": "Enhanced Safety",
            "text": "Reduce the risk of electrical fires and overheating by replacing outdated, ungrounded wiring.",
        },
        {
            "title": "Increased Home Value",
            "text": "Updated wiring is a major selling point for buyers and may improve home insurance eligibility.",
        },
        {
            "title": "Better Power Capacity",
            "text": "Modern wiring supports today’s electrical loads, reducing overloads and power interruptions.",
        },
    ]
    existing_bullets = set(
        BulletPoint.objects.filter(service=service).values_list("title", flat=True)
    )
    for b in bullets:
        if b["title"] not in existing_bullets:
            BulletPoint.objects.create(service=service, title=b["title"], text=b["text"])

    # FAQs (dedupe by question)
    faqs = [
        {
            "question": "Why is knob and tube wiring dangerous?",
            "answer": (
                "Knob and tube lacks grounding, has insulation that can degrade over time, and was never designed to "
                "handle modern electrical loads — all of which can increase fire and shock risks."
            ),
        },
        {
            "question": "How much does it cost to replace knob and tube wiring?",
            "answer": (
                "The cost depends on the size and complexity of your home, but we provide free consultations and "
                "detailed estimates so you know exactly what to expect."
            ),
        },
        {
            "question": "Do I need to replace all the knob and tube at once?",
            "answer": (
                "While it’s safest to fully replace it, we can help assess your system and prioritize critical areas "
                "if a phased approach is needed."
            ),
        },
    ]
    existing_faqs = set(
        FAQ.objects.filter(service=service).values_list("question", flat=True)
    )
    for f in faqs:
        if f["question"] not in existing_faqs:
            FAQ.objects.create(service=service, question=f["question"], answer=f["answer"])


def remove_knob_and_tube_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    service = Service.objects.filter(slug="knob-and-tube-wiring-replacement").first()
    if service:
        service.delete()


class Migration(migrations.Migration):

    dependencies = [
        # 👇 Replace with your latest migration in the "core" app
        ("core", "0005_auto_20250906_1512"),
    ]

    operations = [
        migrations.RunPython(add_knob_and_tube_service, remove_knob_and_tube_service),
    ]
