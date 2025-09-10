from django.db import migrations


def add_design_build_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    BulletPoint = apps.get_model("core", "BulletPoint")
    FAQ = apps.get_model("core", "FAQ")

    slug = "design-build-electrical-projects"

    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            "title": "Design-Build Electrical Projects",
            "subtitle": "From concept to completion, we handle all aspects of custom electrical design and installation.",
            "intro_heading": "Seamless Electrical Design and Installation, Start to Finish",
            "intro_body": (
                "At ACS Electrical Contractors, we specialize in full-service design-build electrical projects that take your vision "
                "from concept to completion. Serving residential, commercial, and industrial clients across Maine, we "
                "combine expert electrical design, precise installation, and seamless project management to deliver "
                "safe, efficient, and code-compliant results. Whether you’re planning a new construction, renovation, "
                "or specialized build, our team ensures every detail is thoughtfully engineered and expertly executed."
            ),
            "why_heading": "Why Choose ACS Electrical Contractors for Design-Build Electrical Projects?",
            "why_body": (
                "Choosing a design-build approach means you get streamlined communication, faster project timelines, "
                "and a single team accountable for both design and execution. At ACS Electrical Contractors, we bring decades of "
                "experience, technical expertise, and a commitment to safety and quality on every project. Our "
                "integrated process helps reduce costs, avoid delays, and ensure your electrical system is perfectly "
                "matched to your needs — today and into the future."
            ),
            "image": 'img/design-build-electrical.png',
        },
    )

    # keep fields fresh if record already exists
    if not created:
        service.title = "Design-Build Electrical Projects"
        service.intro_heading = "Seamless Electrical Design and Installation, Start to Finish"
        service.intro_body = (
            "At ACS Electrical Contractors, we specialize in full-service design-build electrical projects that take your vision "
            "from concept to completion. Serving residential, commercial, and industrial clients across Maine, we "
            "combine expert electrical design, precise installation, and seamless project management to deliver "
            "safe, efficient, and code-compliant results. Whether you’re planning a new construction, renovation, "
            "or specialized build, our team ensures every detail is thoughtfully engineered and expertly executed."
        )
        service.why_heading = "Why Choose ACS Electrical Contractors for Design-Build Electrical Projects?"
        service.why_body = (
            "Choosing a design-build approach means you get streamlined communication, faster project timelines, "
            "and a single team accountable for both design and execution. At ACS Electrical Contractors, we bring decades of "
            "experience, technical expertise, and a commitment to safety and quality on every project. Our "
            "integrated process helps reduce costs, avoid delays, and ensure your electrical system is perfectly "
            "matched to your needs — today and into the future."
        )
        service.save(update_fields=["title", "intro_heading", "intro_body", "why_heading", "why_body"])

    # Bullet points (dedupe by title)
    bullets = [
        {
            "title": "Streamlined Process",
            "text": "One team handles design and installation, minimizing miscommunication and saving you time.",
        },
        {
            "title": "Cost-Effective Solutions",
            "text": "Early collaboration allows for smarter planning, reducing change orders and unexpected costs.",
        },
        {
            "title": "High-Quality Results",
            "text": "With our deep experience and focus on safety, you get an electrical system built to last and meet code.",
        },
    ]
    existing_bullets = set(BulletPoint.objects.filter(service=service).values_list("title", flat=True))
    for b in bullets:
        if b["title"] not in existing_bullets:
            BulletPoint.objects.create(service=service, title=b["title"], text=b["text"])

    # FAQs (dedupe by question)
    faqs = [
        {
            "question": "How is a design-build electrical project different from a traditional project?",
            "answer": (
                "In a traditional setup, you hire a designer or engineer separately from the contractor, which can lead "
                "to miscommunications or design changes during construction. With design-build, ACS Electrical Contractors handles both "
                "the design and the installation, ensuring smoother coordination, fewer delays, and a more efficient process."
            ),
        },
        {
            "question": "How much do design-build electrical projects cost?",
            "answer": (
                "Costs vary depending on the size and complexity of your project, but design-build often saves money by "
                "reducing change orders and avoiding costly miscommunications. We’re happy to provide a free consultation "
                "and estimate tailored to your needs."
            ),
        },
        {
            "question": "What types of projects are best for design-build?",
            "answer": (
                "Design-build works especially well for new construction, renovations, or custom electrical systems where "
                "you want one team to manage everything from planning to final installation. It’s ideal for homeowners, "
                "business owners, and developers looking for efficiency and accountability."
            ),
        },
    ]
    existing_faqs = set(FAQ.objects.filter(service=service).values_list("question", flat=True))
    for f in faqs:
        if f["question"] not in existing_faqs:
            FAQ.objects.create(service=service, question=f["question"], answer=f["answer"])


def remove_design_build_service(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    svc = Service.objects.filter(slug="design-build-electrical-projects").first()
    if svc:
        svc.delete()


class Migration(migrations.Migration):

    dependencies = [
        # 🔁 Replace with your latest migration in the "core" app
        ("core", "0007_auto_20250906_1522"),
    ]

    operations = [
        migrations.RunPython(add_design_build_service, remove_design_build_service),
    ]
