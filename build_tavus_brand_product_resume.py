from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Table, TableStyle


OUT = Path("output/pdf")
OUT.mkdir(parents=True, exist_ok=True)

INK = HexColor("#171D2B")
MUTED = HexColor("#596174")
VIOLET = HexColor("#6046C8")
LINE = HexColor("#D7D3E6")


def link(url, label):
    return f'<link href="{url}" color="#6046C8"><u>{label}</u></link>'


def table_no_padding(rows, widths):
    table = Table(rows, colWidths=widths)
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return table


def build():
    path = OUT / "Haylie-Wong-Tavus-Brand-Product-Designer-Resume.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=letter,
        leftMargin=.62 * inch, rightMargin=.62 * inch,
        topMargin=.34 * inch, bottomMargin=.27 * inch,
        title="Haylie Wong - Brand & Product Designer Resume",
        author="Haylie Wong",
        subject="Application for Brand & Product Designer at Tavus",
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=25, leading=27, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Tag", fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=VIOLET, spaceAfter=2))
    styles.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=7.75, leading=9.4, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=10.25, leading=11.7, textColor=VIOLET, spaceBefore=4.5, spaceAfter=1.8))
    styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=7.55, leading=9.05, textColor=INK, spaceAfter=1.25))
    styles.add(ParagraphStyle(name="Summary", parent=styles["Body"], fontSize=7.95, leading=9.55))
    styles.add(ParagraphStyle(name="Role", fontName="Helvetica-Bold", fontSize=8.55, leading=9.8, textColor=INK, spaceAfter=.35))
    styles.add(ParagraphStyle(name="Meta", fontName="Helvetica", fontSize=7.25, leading=8.45, textColor=MUTED, spaceAfter=.8))
    styles.add(ParagraphStyle(name="Date", fontName="Helvetica-Bold", fontSize=7.2, leading=8.8, textColor=VIOLET))

    story = [
        Paragraph("HAYLIE WONG", styles["Name"]),
        Paragraph("BRAND & PRODUCT DESIGN | VISUAL STORYTELLING | AI-ASSISTED CREATION", styles["Tag"]),
        Paragraph(
            "Relocating to San Francisco, CA | Housing secured | Requires employer-sponsored U.S. work authorization<br/>"
            "hayliewsw@gmail.com | "
            + link("https://www.linkedin.com/in/hayliewsw/", "linkedin.com/in/hayliewsw") + " | "
            + link("https://hayliewsw.github.io/portfolio/", "hayliewsw.github.io/portfolio"),
            styles["Contact"],
        ),
        HRFlowable(width="100%", thickness=.7, color=LINE, spaceBefore=2, spaceAfter=3),
        Paragraph("PROFILE", styles["Section"]),
        Paragraph(
            "Multidisciplinary designer with four years of UX/UI and digital product experience, complemented by senior copywriting, art direction, and hands-on AI-assisted creation. I connect brand expression with product experience, translating complex ideas into distinctive visual systems, clear narratives, and polished interactions across web, mobile, and games. My end-to-end practice spans research, information architecture, design systems, prototypes, production specifications, storytelling, and iterative testing.",
            styles["Summary"],
        ),
        Paragraph("CORE CAPABILITIES", styles["Section"]),
        Paragraph(
            "Brand expression & visual storytelling  |  Product and UX/UI design  |  Art direction  |  Responsive web design<br/>"
            "Design systems & interaction patterns  |  Typography, layout & hierarchy  |  Figma  |  Prototyping<br/>"
            "Content hierarchy & product storytelling  |  Usability testing  |  Developer collaboration  |  AI-assisted building",
            styles["Body"],
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]),
    ]

    entries = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada",
         "Shape the studio's creative identity and player experience, leading art direction and game UX from early concepts through playtesting. Partner with development to turn narrative, visual, and interaction ideas into a cohesive playable product."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote",
         "Develop original game concepts through visual direction, interaction design, onboarding, prototyping, and iterative playtesting. Use Figma, Godot, GitHub, and generative tools to move rapidly from story and mood to tangible experiences."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore",
         "Translate complex, high-stakes topics into clear, audience-aware content. Adapt voice, hierarchy, and detail to customer needs while maintaining accuracy, discretion, and a consistent narrative across communications."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore",
         "Owned end-to-end UX for a shipped profile revamp, creating flows, interaction patterns, prototypes, states, and production specifications. Collaborated across product, engineering, marketing, and data, using moderated research to align customer insight with product direction."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore",
         "Designed responsive digital experiences that translated client brands, business goals, and information architecture into polished interfaces. Created visual systems, page structures, prototypes, and build-ready specifications with project managers and developers."),
    ]

    for date, role, org, body in entries:
        details = [Paragraph(role, styles["Role"]), Paragraph(org, styles["Meta"]), Paragraph(body, styles["Body"])]
        story.append(KeepTogether(table_no_padding([[Paragraph(date, styles["Date"]), details]], [.9 * inch, 6.05 * inch])))

    story += [Paragraph("SELECTED WORK", styles["Section"])]
    projects = [
        ("abillion Profile Revamp | Product Design & Research",
         "Sole UX designer for a launched profile revamp; defined systems, flows, prototypes, and specifications, then validated the experience with four participants across eight tasks."),
        ("Sompo Asia Website Revamp | Brand, Responsive UI & Information Architecture",
         "Translated a refreshed brand into a complete regional website across desktop and mobile, connecting clearer information architecture with polished, production-ready visual execution."),
        ("Toadally In Love | Art Direction & Game UX",
         "Led the visual direction and UX for a four-day puzzle-game build, creating a readable interaction language and cohesive world that ranked third overall among 73 entries."),
        ("Inventory Management System | Product Design & AI-Assisted Build",
         "Identified, designed, built, and iterated a working inventory website in five days, transforming CSV and Notion data into clear filters, categories, and location-aware views."),
    ]
    for title, body in projects:
        story.append(KeepTogether([Paragraph(title, styles["Role"]), Paragraph(body, styles["Body"])]))

    story += [
        Paragraph("EDUCATION", styles["Section"]),
        table_no_padding([
            [Paragraph("2022 - 2023", styles["Date"]), [Paragraph("Design Management, Post-graduate Certificate", styles["Role"]), Paragraph("George Brown College | Dean's List", styles["Meta"])]],
            [Paragraph("2016 - 2017", styles["Date"]), [Paragraph("Bachelor of Communication, Professional Communications", styles["Role"]), Paragraph("RMIT University | Singapore & Australia", styles["Meta"])]],
        ], [.9 * inch, 6.05 * inch]),
    ]

    doc.build(story)
    return path


if __name__ == "__main__":
    print(build())
