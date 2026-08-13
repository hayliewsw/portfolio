from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Table, TableStyle


OUT = Path("output/pdf")
OUT.mkdir(parents=True, exist_ok=True)

INK = HexColor("#16251F")
MUTED = HexColor("#58665F")
GREEN = HexColor("#19724F")
LINE = HexColor("#CEDBD4")


def link(url, label):
    return f'<link href="{url}" color="#19724F"><u>{label}</u></link>'


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
    path = OUT / "Haylie-Wong-Thatch-Product-Designer-Resume.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=letter,
        leftMargin=.62 * inch, rightMargin=.62 * inch,
        topMargin=.34 * inch, bottomMargin=.27 * inch,
        title="Haylie Wong - Product Designer Resume",
        author="Haylie Wong",
        subject="Application for Product Designer at Thatch",
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=25, leading=27, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Tag", fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=GREEN, spaceAfter=2))
    styles.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=7.75, leading=9.4, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=10.25, leading=11.7, textColor=GREEN, spaceBefore=4.5, spaceAfter=1.8))
    styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=7.55, leading=9.05, textColor=INK, spaceAfter=1.25))
    styles.add(ParagraphStyle(name="Summary", parent=styles["Body"], fontSize=7.95, leading=9.55))
    styles.add(ParagraphStyle(name="Role", fontName="Helvetica-Bold", fontSize=8.55, leading=9.8, textColor=INK, spaceAfter=.35))
    styles.add(ParagraphStyle(name="Meta", fontName="Helvetica", fontSize=7.25, leading=8.45, textColor=MUTED, spaceAfter=.8))
    styles.add(ParagraphStyle(name="Date", fontName="Helvetica-Bold", fontSize=7.2, leading=8.8, textColor=GREEN))

    story = [
        Paragraph("HAYLIE WONG", styles["Name"]),
        Paragraph("PRODUCT DESIGN | COMPLEX WORKFLOWS | DESIGN SYSTEMS", styles["Tag"]),
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
            "Product designer with four years of UX/UI and digital product experience across mobile and responsive web. I turn complex workflows, sensitive information, and operational requirements into clear, trustworthy end-to-end experiences. My practice spans research, product strategy, information architecture, user flows, design systems, prototypes, production specifications, and usability testing. I work closely with product, engineering, marketing, data, and operations to balance customer needs, business constraints, craft, and momentum.",
            styles["Summary"],
        ),
        Paragraph("CORE CAPABILITIES", styles["Section"]),
        Paragraph(
            "End-to-end product design  |  Complex and multi-step workflows  |  UX strategy  |  Information architecture<br/>"
            "Design systems, components & interaction patterns  |  Responsive UI  |  Figma  |  Flows and prototypes<br/>"
            "Usability testing  |  Design documentation  |  Production specifications  |  Developer collaboration  |  AI-assisted building",
            styles["Body"],
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]),
    ]

    entries = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada",
         "Lead game UX and art direction from concept through playtesting, partnering with development to turn open-ended ideas into coherent interactions. Define priorities, test assumptions, and iterate onboarding and feedback systems from observed player behavior."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote",
         "Design and playtest interactive experiences across flows, rules, visual systems, onboarding, and moment-to-moment feedback. Use Figma, Godot, GitHub, and AI-assisted tools to prototype quickly and collaborate closely with development."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore",
         "Translate complex, high-stakes immigration topics into clear, audience-aware guidance. Structure sensitive information around user needs while maintaining accuracy, discretion, consistency, and trust."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore",
         "Owned end-to-end UX for a shipped profile revamp, defining information architecture, flows, states, interaction patterns, prototypes, and production specifications. Partnered across product, engineering, marketing, and data; planned moderated research and translated findings into product decisions."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore",
         "Designed responsive web experiences by translating brand, business, and information-architecture needs into clear journeys and polished interfaces. Delivered prototypes, UI systems, responsive states, and build-ready specifications with clients, project managers, and developers."),
    ]

    for date, role, org, body in entries:
        details = [Paragraph(role, styles["Role"]), Paragraph(org, styles["Meta"]), Paragraph(body, styles["Body"])]
        story.append(KeepTogether(table_no_padding([[Paragraph(date, styles["Date"]), details]], [.9 * inch, 6.05 * inch])))

    story += [Paragraph("SELECTED PRODUCT WORK", styles["Section"])]
    projects = [
        ("abillion Profile Revamp | End-to-End Product Design",
         "Sole UX designer for a launched profile revamp. Defined interconnected content, privacy, and interaction states; produced flows, prototypes, and specifications; and validated the proposed experience with four participants across eight tasks."),
        ("Inventory Management System | Operational Workflow Design",
         "Identified, designed, built, and iterated a working inventory website in five days, transforming CSV and Notion data into clear categories, filters, and location-aware views for tracking stock and sales."),
        ("Sompo Asia Website Revamp | Responsive UI & Information Architecture",
         "Designed a complete regional website across desktop and mobile, translating a refreshed brand and complex content structure into clearer journeys, responsive states, and production-ready specifications."),
        ("Mad John | Iterative Game UX",
         "Led UX and art direction for an in-progress card-and-puzzle game, using six mixed-experience playtests to introduce a hands-on tutorial and refine comprehension, scoring, and player feedback."),
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
