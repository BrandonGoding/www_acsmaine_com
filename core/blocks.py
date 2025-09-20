from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroWithBulletsBlock(blocks.StructBlock):
    tagline = blocks.CharBlock(
        required=False,
        help_text="Small tagline above the title (e.g. 'Pride in Professionalism, Quality and Service')."
    )
    title = blocks.CharBlock(
        required=True,
        help_text="Main headline (e.g. 'ACS Electrical Contractors')."
    )
    description = blocks.TextBlock(
        required=False,
        help_text="Supporting text/intro paragraph."
    )

    urgent_contact_button_text = blocks.CharBlock(required=True, help_text="Example: 'Call Now'")
    urgent_contact_phone_number = blocks.CharBlock(required=False, help_text="Example: tel:2077823001")
    secondary_button_text = blocks.CharBlock(required=False)
    secondary_button_url = blocks.PageChooserBlock(required=False)

    bullets = blocks.ListBlock(
        blocks.StructBlock([
            ("text", blocks.CharBlock(required=True)),
        ]),
        help_text="List of value bullets (e.g. Experienced Team, Safety First)."
    )

    image = ImageChooserBlock(required=True, help_text="Hero image on the right side.")
    experience_years = blocks.CharBlock(
        required=False,
        help_text="Years of experience badge (e.g. '30+')."
    )
    experience_text = blocks.CharBlock(
        required=False,
        help_text="Experience caption (e.g. 'Years of experience, Lewiston–Auburn & beyond')."
    )

    class Meta:
        template = "blocks/hero_with_bullets.html"
        icon = "placeholder"
        label = "Hero With Bullets"
