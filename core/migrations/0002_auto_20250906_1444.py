from django.db import migrations


def add_pools_saunas_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    service, created = Service.objects.get_or_create(
        slug="sauna-pool-jacuzzi",
        defaults={
            "title": "Sauna, Pool & Jacuzzi Electrical Work",
            "subtitle": "Specialized wiring and safety installations for wet and high‑moisture environments.",
            "intro_heading": "Sauna, Pool, and Jacuzzi Electrical Installation in Maine",
            "intro_body": "ACS Maine provides specialized electrical services for saunas, pools, hot tubs, and Jacuzzis...",
            "why_heading": "Why Trust ACS for Your Spa & Pool Electrical Work?",
            "why_body": "Working with water and electricity demands experience, attention to detail, and a deep understanding of safety codes...",
            "image": "img/pool-and-j.png",
        },
    )

    if created:
        bullets = [
            {"title": "Code-Compliant & Inspected", "text": "We ensure your setup meets NEC and Maine electrical safety standards."},
            {"title": "Peace of Mind Around Water", "text": "GFCI protection and proper grounding keep your family and guests safe."},
            {"title": "Complete Integration", "text": "We handle pumps, heaters, lights, timers, and control systems — wired right the first time."},
        ]
        for b in bullets:
            BulletPoint.objects.create(service=service, title=b["title"], text=b["text"])

        faqs = [
            {"question": "Do I need a dedicated circuit for my hot tub or pool?", "answer": "Yes. Dedicated circuits + GFCI + bonding are typically required."},
            {"question": "Can you wire both indoor and outdoor spa features?", "answer": "Absolutely. We protect wiring from moisture, corrosion, and weather."},
            {"question": "How soon can you install?", "answer": "We coordinate with your delivery/installer for a fast, clean install."},
        ]
        for f in faqs:
            FAQ.objects.create(service=service, question=f["question"], answer=f["answer"])


def remove_pools_saunas_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    service = Service.objects.filter(slug="sauna-pool-jacuzzi").first()
    if service:
        service.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_pools_saunas_service, remove_pools_saunas_service),
    ]
