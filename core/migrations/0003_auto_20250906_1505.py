from django.db import migrations


def add_wiring_new_builds_remodels(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    slug = "wiring-new-buildings-remodels"

    # Upsert the Service
    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            "title": "Wiring for New Buildings & Remodels",
            "intro_heading": "Electrical Wiring for New Construction and Remodels",
            "intro_body": (
                "ACS Electrical Contractors provides complete electrical wiring for new buildings and remodels, "
                "ensuring your system is designed and installed to meet today’s safety codes, power needs, and future "
                "expansions. Whether you’re constructing a brand-new home, renovating a commercial space, or reworking "
                "part of your property, our licensed electricians deliver clean, efficient, and code-compliant wiring — "
                "built to handle modern life from the ground up."
            ),
            "why_heading": "Why Trust ACS with Your Wiring Project?",
            "why_body": (
                "Wiring is the backbone of any structure — and doing it right from the start prevents costly fixes down "
                "the road. At ACS, we plan every circuit, outlet, and fixture placement with care, using quality materials "
                "and modern techniques. We collaborate with contractors, builders, and homeowners to ensure every part of "
                "your electrical system supports your goals and passes inspection the first time."
            ),
            # No image provided in the snippet; leave null/blank per model definition
            "image": None,
        },
    )

    # If it already existed, keep fields fresh (idempotent upsert behavior)
    if not created:
        service.title = "Wiring for New Buildings & Remodels"
        service.intro_heading = "Electrical Wiring for New Construction and Remodels"
        service.intro_body = (
            "ACS Electrical Contractors provides complete electrical wiring for new buildings and remodels, "
            "ensuring your system is designed and installed to meet today’s safety codes, power needs, and future "
            "expansions. Whether you’re constructing a brand-new home, renovating a commercial space, or reworking "
            "part of your property, our licensed electricians deliver clean, efficient, and code-compliant wiring — "
            "built to handle modern life from the ground up."
        )
        service.why_heading = "Why Trust ACS with Your Wiring Project?"
        service.why_body = (
            "Wiring is the backbone of any structure — and doing it right from the start prevents costly fixes down "
            "the road. At ACS, we plan every circuit, outlet, and fixture placement with care, using quality materials "
            "and modern techniques. We collaborate with contractors, builders, and homeowners to ensure every part of "
            "your electrical system supports your goals and passes inspection the first time."
        )
        service.save(update_fields=["title", "intro_heading", "intro_body", "why_heading", "why_body"])

    # Seed bullet points (ensure no duplicates by title)
    bullets = [
        {
            "title": "Customized Wiring Plans",
            "text": "We tailor the layout to your floor plan, room usage, and future technology needs.",
        },
        {
            "title": "Safe, Code-Compliant Installation",
            "text": "All work is completed to NEC and Maine electrical code standards.",
        },
        {
            "title": "One Team, Start to Finish",
            "text": "From rough-in to final fixture.",
        },
    ]
    existing_titles = set(
        BulletPoint.objects.filter(service=service).values_list("title", flat=True)
    )
    for b in bullets:
        if b["title"] not in existing_titles:
            BulletPoint.objects.create(service=service, title=b["title"], text=b["text"])

    # Seed FAQs (ensure no duplicates by question)
    faqs = [
        {
            "question": "When should I bring in an electrician during a remodel or new build?",
            "answer": (
                "It’s best to involve us early — ideally during planning or framing. This allows us to coordinate with "
                "your builder and ensure a smooth rough-in and finish phase."
            ),
        },
        {
            "question": "Can you upgrade wiring during a remodel without tearing out all the walls?",
            "answer": (
                "Yes. We specialize in remodeling projects and use minimally invasive techniques to upgrade wiring while "
                "preserving finished surfaces whenever possible."
            ),
        },
        {
            "question": "Do I need permits or inspections?",
            "answer": (
                "Yes, and we handle all permitting and inspection scheduling as part of the job — so you stay compliant "
                "without the hassle."
            ),
        },
    ]
    existing_questions = set(
        FAQ.objects.filter(service=service).values_list("question", flat=True)
    )
    for f in faqs:
        if f["question"] not in existing_questions:
            FAQ.objects.create(service=service, question=f["question"], answer=f["answer"])


def remove_wiring_new_builds_remodels(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    service = Service.objects.filter(slug="wiring-new-buildings-remodels").first()
    if service:
        service.delete()


class Migration(migrations.Migration):

    dependencies = [
        # 🔁 Replace with your latest migration in the "core" app
        ("core", "0002_auto_20250906_1444"),
    ]

    operations = [
        migrations.RunPython(add_wiring_new_builds_remodels, remove_wiring_new_builds_remodels),
    ]
