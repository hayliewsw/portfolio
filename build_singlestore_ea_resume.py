from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Table, TableStyle


OUT = Path("output/pdf")
OUT.mkdir(parents=True, exist_ok=True)

INK = HexColor("#182320")
MUTED = HexColor("#52615D")
GREEN = HexColor("#24624F")
LINE = HexColor("#CAD6D1")


def link(url, label):
    return f'<link href="{url}" color="#24624F"><u>{label}</u></link>'


def no_padding_table(rows, widths):
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
    path = OUT / "Haylie-Wong-SingleStore-Executive-Assistant-Resume.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=letter,
        leftMargin=.62 * inch, rightMargin=.62 * inch,
        topMargin=.35 * inch, bottomMargin=.28 * inch,
        title="Haylie Wong - Executive Assistant Resume",
        author="Haylie Wong",
        subject="Application for Executive Assistant at SingleStore",
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=25, leading=27, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Tag", fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=GREEN, spaceAfter=2))
    styles.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=7.8, leading=9.5, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=10.3, leading=12, textColor=GREEN, spaceBefore=5, spaceAfter=2))
    styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=7.65, leading=9.25, textColor=INK, spaceAfter=1.4))
    styles.add(ParagraphStyle(name="Summary", parent=styles["Body"], fontSize=8.05, leading=9.8))
    styles.add(ParagraphStyle(name="Role", fontName="Helvetica-Bold", fontSize=8.7, leading=10, textColor=INK, spaceAfter=.4))
    styles.add(ParagraphStyle(name="Meta", fontName="Helvetica", fontSize=7.35, leading=8.6, textColor=MUTED, spaceAfter=1))
    styles.add(ParagraphStyle(name="Date", fontName="Helvetica-Bold", fontSize=7.25, leading=9, textColor=GREEN))

    story = [
        Paragraph("HAYLIE WONG", styles["Name"]),
        Paragraph("EXECUTIVE SUPPORT | OPERATIONS | COMMUNICATIONS", styles["Tag"]),
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
            "Executive support and operations professional with experience coordinating leadership priorities, scheduling, communications, and stakeholder workflows in fast-moving environments. Brings sound judgment, discretion with sensitive information, and a builder mindset shaped by work across executive support, senior copywriting, product design, and entrepreneurship. Known for turning ambiguity and complex information into clear systems, dependable deliverables, and aligned action.",
            styles["Summary"],
        ),
        Paragraph("CORE CAPABILITIES", styles["Section"]),
        Paragraph(
            "Executive scheduling and priority coordination  |  Executive-ready communications  |  Stakeholder alignment<br/>"
            "Confidential information handling  |  Project and workflow coordination  |  Documentation  |  Problem solving<br/>"
            "Cross-functional collaboration  |  Research and synthesis  |  Process improvement  |  AI-assisted productivity",
            styles["Body"],
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]),
    ]

    entries = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada",
         "Coordinate creative and product priorities for an independent game studio, partnering with development from concept through playtesting. Bring structure to open-ended work, maintain alignment on decisions, and move projects forward through clear communication and hands-on execution."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote",
         "Plan and execute multidisciplinary projects across design, prototyping, feedback, and iteration. Coordinate with collaborators, organize evolving requirements, and use AI-assisted tools to accelerate research, documentation, and production."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore",
         "Translate complex, high-stakes immigration information into accurate, audience-aware communications. Manage sensitive client information with discretion, adapt quickly to changing requirements, and maintain clarity and consistency across deliverables."),
        ("2023 - 2024", "Executive Assistant", "ed&amp;c | Singapore",
         "Coordinated executive priorities, scheduling, communications, stakeholder updates, and operational workflows. Kept information and follow-through organized across competing needs while handling confidential matters with care and professional judgment."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore",
         "Owned end-to-end UX for a launched profile revamp and coordinated work across product, engineering, marketing, and data. Synthesized stakeholder and customer input into clear priorities, documentation, prototypes, specifications, and launch-ready decisions."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore",
         "Managed detailed design deliverables across client, project-management, and development stakeholders. Converted business goals and complex information into organized workflows, responsive interfaces, prototypes, and build-ready specifications."),
    ]

    for date, role, org, body in entries:
        details = [Paragraph(role, styles["Role"]), Paragraph(org, styles["Meta"]), Paragraph(body, styles["Body"])]
        story.append(KeepTogether(no_padding_table([[Paragraph(date, styles["Date"]), details]], [.9 * inch, 6.05 * inch])))

    story += [
        Paragraph("SELECTED OPERATIONAL PROJECT", styles["Section"]),
        KeepTogether([
            Paragraph("Inventory Management System | Independent", styles["Role"]),
            Paragraph(
                "Identified an operational need and designed, built, and iterated a working inventory website in five days. Transformed CSV and Notion data into clear categories, filters, and location-aware views for tracking stock and sales.",
                styles["Body"],
            ),
        ]),
        Paragraph("EDUCATION", styles["Section"]),
        no_padding_table([
            [Paragraph("2022 - 2023", styles["Date"]), [Paragraph("Design Management, Post-graduate Certificate", styles["Role"]), Paragraph("George Brown College | Dean's List", styles["Meta"])]],
            [Paragraph("2016 - 2017", styles["Date"]), [Paragraph("Bachelor of Communication, Professional Communications", styles["Role"]), Paragraph("RMIT University | Singapore & Australia", styles["Meta"])]],
        ], [.9 * inch, 6.05 * inch]),
    ]

    doc.build(story)
    return path


if __name__ == "__main__":
    print(build())
