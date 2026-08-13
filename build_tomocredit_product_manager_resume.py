from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Table, TableStyle


OUT = Path("output/pdf")
OUT.mkdir(parents=True, exist_ok=True)

INK = HexColor("#17212A")
MUTED = HexColor("#58646D")
BLUE = HexColor("#176B87")
LINE = HexColor("#CCD9DE")


def link(url, label):
    return f'<link href="{url}" color="#176B87"><u>{label}</u></link>'


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
    path = OUT / "Haylie-Wong-TomoCredit-Product-Manager-Resume.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=letter,
        leftMargin=.62 * inch, rightMargin=.62 * inch,
        topMargin=.34 * inch, bottomMargin=.27 * inch,
        title="Haylie Wong - Product Manager Resume",
        author="Haylie Wong",
        subject="Application for Product Manager at TomoCredit",
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=25, leading=27, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Tag", fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=BLUE, spaceAfter=2))
    styles.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=7.75, leading=9.4, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=10.25, leading=11.7, textColor=BLUE, spaceBefore=4.5, spaceAfter=1.8))
    styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=7.55, leading=9.05, textColor=INK, spaceAfter=1.25))
    styles.add(ParagraphStyle(name="Summary", parent=styles["Body"], fontSize=7.95, leading=9.55))
    styles.add(ParagraphStyle(name="Role", fontName="Helvetica-Bold", fontSize=8.55, leading=9.8, textColor=INK, spaceAfter=.35))
    styles.add(ParagraphStyle(name="Meta", fontName="Helvetica", fontSize=7.25, leading=8.45, textColor=MUTED, spaceAfter=.8))
    styles.add(ParagraphStyle(name="Date", fontName="Helvetica-Bold", fontSize=7.2, leading=8.8, textColor=BLUE))

    story = [
        Paragraph("HAYLIE WONG", styles["Name"]),
        Paragraph("PRODUCT OWNERSHIP | CUSTOMER INSIGHT | AI-ASSISTED BUILDING", styles["Tag"]),
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
            "Product-minded designer and hands-on builder with four years of digital product experience across mobile and responsive web. I have owned shipped experiences from customer research and problem definition through workflows, product decisions, specifications, cross-functional delivery, usability testing, and launch. My background combines systems thinking, clear stakeholder communication, operational problem solving, and growing technical fluency through AI-assisted development, Godot, and GitHub.",
            styles["Summary"],
        ),
        Paragraph("CORE CAPABILITIES", styles["Section"]),
        Paragraph(
            "End-to-end product ownership  |  Customer research & usability testing  |  Opportunity and problem definition<br/>"
            "Feature prioritization & tradeoffs  |  Product requirements & specifications  |  Complex workflow design<br/>"
            "Cross-functional delivery  |  Stakeholder communication  |  Rapid prototyping  |  Figma  |  Godot  |  GitHub  |  AI-assisted development",
            styles["Body"],
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]),
    ]

    entries = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada",
         "Shape product direction and player experience for an independent game studio. Define priorities, make scope and interaction decisions, coordinate with development, and use playtesting feedback to iterate onboarding, gameplay, and product quality."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote",
         "Take original product concepts from definition through AI-assisted prototypes and playtests. Design flows, rules, feedback systems, and onboarding; organize evolving requirements and collaborate with development using Figma, Godot, and GitHub."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore",
         "Translate complex, high-stakes immigration information into accurate, audience-aware guidance. Structure ambiguous requirements, adapt communication to customer needs, and handle sensitive information with consistency and sound judgment."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore",
         "Owned end-to-end UX for a shipped profile revamp, moving from customer and business needs through information architecture, flows, states, prototypes, product decisions, and launch-ready specifications. Partnered across product, engineering, marketing, and data and conducted moderated usability research."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore",
         "Translated client goals and complex information into clear responsive product requirements, user journeys, interfaces, and build-ready specifications. Managed detailed deliverables and implementation collaboration across clients, project managers, and developers."),
    ]

    for date, role, org, body in entries:
        details = [Paragraph(role, styles["Role"]), Paragraph(org, styles["Meta"]), Paragraph(body, styles["Body"])]
        story.append(KeepTogether(table_no_padding([[Paragraph(date, styles["Date"]), details]], [.9 * inch, 6.05 * inch])))

    story += [Paragraph("SELECTED PRODUCT WORK", styles["Section"])]
    projects = [
        ("abillion Profile Revamp | Shipped Consumer Product",
         "Sole UX designer for a launched profile revamp. Defined interconnected content, privacy, and interaction states; aligned stakeholders around flows and specifications; and validated the proposed experience with four participants across eight tasks."),
        ("Inventory Management System | Operational Product Build",
         "Identified an inventory problem and designed, built, and iterated a working website in five days, converting CSV and Notion data into useful categories, filters, and location-aware views for tracking stock and sales."),
        ("Mad John | Product Iteration Through Playtesting",
         "Led product experience and art direction for a card-and-puzzle game, using six mixed-experience playtests to identify comprehension problems, introduce a hands-on tutorial, and refine scoring and feedback."),
        ("Toadally In Love | Rapid Cross-Functional Launch",
         "Led UX and art direction for a four-day game build, making fast scope and interaction decisions with development; the finished experience ranked third overall among 73 entries."),
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
