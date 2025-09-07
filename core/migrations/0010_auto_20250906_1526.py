from django.db import migrations


def add_fuse_to_breaker_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    slug = "fuse-to-circuit-breaker-upgrades"

    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            "title": "Fuse to Circuit Breaker Upgrades",
            "subtitle": "Upgrade old fuse boxes to modern circuit breaker panels for safety and reliability.",
            "intro_heading": "Fuse Box to Circuit Breaker Upgrades in Maine",
            "intro_body": (
                "At ACS Electrical Contractors, we specialize in fuse box to circuit breaker upgrades that improve the "
                "safety, reliability, and efficiency of your electrical system. Older fuse boxes were designed for much "
                "lower electrical loads than today’s homes and businesses demand. Our expert team will assess your current "
                "setup and upgrade it to a modern circuit breaker panel, giving you peace of mind and protecting your "
                "property from electrical hazards."
            ),
            "why_heading": "Why Upgrade with ACS?",
            "why_body": (
                "Upgrading from fuses to circuit breakers isn’t just about convenience — it’s about safety and future "
                "readiness. ACS Maine ensures your upgrade is performed to the highest standards, helping prevent "
                "electrical fires, reduce maintenance headaches, and increase the overall value of your home or "
                "commercial property."
            ),
            "image": "img/fuse-to-circuit-breaker-upgrades.png",
        },
    )

    # If it already exists, keep fields fresh (idempotent upsert)
    if not created:
        service.title = "Fuse to Circuit Breaker Upgrades"
        service.intro_heading = "Fuse Box to Circuit Breaker Upgrades in Maine"
        service.intro_body = (
            "At ACS Electrical Contractors, we specialize in fuse box to circuit breaker upgrades that improve the "
            "safety, reliability, and efficiency of your electrical system. Older fuse boxes were designed for much "
            "lower electrical loads than today’s homes and businesses demand. Our expert team will assess your current "
            "setup and upgrade it to a modern circuit breaker panel, giving you peace of mind and protecting your "
            "property from electrical hazards."
        )
        service.why_heading = "Why Upgrade with ACS?"
        service.why_body = (
            "Upgrading from fuses to circuit breakers isn’t just about convenience — it’s about safety and future "
            "readiness. ACS Maine ensures your upgrade is performed to the highest standards, helping prevent "
            "electrical fires, reduce maintenance headaches, and increase the overall value of your home or "
            "commercial property."
        )
        service.save(update_fields=["title", "intro_heading", "intro_body", "why_heading", "why_body"])

    # Bullet points (dedupe by title)
    bullets = [
        {"title": "Improved Safety", "text": "Modern circuit breakers provide better overload and short-circuit protection, reducing fire risks."},
        {"title": "Increased Capacity", "text": "Upgrade to handle today’s electrical demands, from appliances to electronics."},
        {"title": "Convenience & Savings", "text": "Easily reset breakers instead of replacing blown fuses, saving time and hassle."},
    ]
    existing_titles = set(BulletPoint.objects.filter(service=service).values_list("title", flat=True))
    for b in bullets:
        if b["title"] not in existing_titles:
            BulletPoint.objects.create(service=service, title=b["title"], text=b["text"])

    # FAQs (dedupe by question)
    faqs = [
        {
            "question": "Why should I upgrade from fuses to circuit breakers?",
            "answer": (
                "Older fuse boxes weren’t designed to handle the electrical loads of modern homes and businesses. "
                "Upgrading improves safety, increases capacity, and makes your system easier to manage."
            ),
        },
        {
            "question": "How much does it cost to upgrade a fuse box?",
            "answer": (
                "Costs vary depending on panel size and complexity, but we offer free consultations to assess your "
                "system and provide a detailed estimate."
            ),
        },
        {
            "question": "Will the upgrade require shutting off power?",
            "answer": (
                "Yes, but only temporarily. We’ll coordinate the upgrade to minimize downtime and complete the work "
                "efficiently and safely."
            ),
        },
    ]
    existing_questions = set(FAQ.objects.filter(service=service).values_list("question", flat=True))
    for f in faqs:
        if f["question"] not in existing_questions:
            FAQ.objects.create(service=service, question=f["question"], answer=f["answer"])


def remove_fuse_to_breaker_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    svc = Service.objects.filter(slug="fuse-to-circuit-breaker-upgrades").first()
    if svc:
        svc.delete()


class Migration(migrations.Migration):

    dependencies = [
        # 🔁 Replace with your latest migration in the "core" app
        ("core", "0009_auto_20250906_1524"),
    ]

    operations = [
        migrations.RunPython(add_fuse_to_breaker_service, remove_fuse_to_breaker_service),
    ]
