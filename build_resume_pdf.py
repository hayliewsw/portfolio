from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Table, TableStyle


output_path = Path("output/pdf/Haylie-Wong-Resume.pdf")
output_path.parent.mkdir(parents=True, exist_ok=True)

ink = HexColor("#000000")
document = SimpleDocTemplate(
    str(output_path),
    pagesize=letter,
    rightMargin=.7 * inch,
    leftMargin=.7 * inch,
    topMargin=.28 * inch,
    bottomMargin=.28 * inch,
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=27, leading=27, textColor=ink, spaceAfter=5))
styles.add(ParagraphStyle(name="Role", fontName="Helvetica", fontSize=8.2, leading=10.5, textColor=ink, spaceAfter=8))
styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=12, leading=14, textColor=ink, spaceBefore=7, spaceAfter=3, uppercase=True))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=7.9, leading=9.7, textColor=ink, spaceAfter=2))
styles.add(ParagraphStyle(name="Job", fontName="Helvetica-Bold", fontSize=9.1, leading=10.6, textColor=ink, spaceAfter=1))
styles.add(ParagraphStyle(name="Company", fontName="Helvetica", fontSize=7.9, leading=9.4, textColor=ink, spaceAfter=1))
styles.add(ParagraphStyle(name="Date", fontName="Helvetica", fontSize=7.9, leading=9.4, textColor=ink))
styles.add(ParagraphStyle(name="ProjectNumber", fontName="Helvetica", fontSize=7.9, leading=9.4, textColor=ink))
styles.add(ParagraphStyle(name="ProjectMeta", fontName="Helvetica-Bold", fontSize=7.1, leading=8.5, textColor=ink, spaceAfter=1))


def two_column_entry(date, title, organization, description):
    content = [
        Paragraph(title, styles["Job"]),
        Paragraph(organization, styles["Company"]),
        Paragraph(description, styles["Body"]),
    ]
    table = Table([[Paragraph(date, styles["Date"]), content]], colWidths=[.85 * inch, 6.1 * inch])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return KeepTogether(table)


story = [
    Paragraph("HAYLIE WONG", styles["Name"]),
    Paragraph(
        "<b>PRODUCT DESIGNER</b><br/>"
        "TORONTO, ON<br/>"
        "<link href=\"mailto:hayliewsw@gmail.com\">HAYLIEWSW@GMAIL.COM</link> | "
        "<link href=\"https://www.linkedin.com/in/hayliewsw/\">LINKEDIN.COM/IN/HAYLIEWSW</link> | "
        "<link href=\"https://hayliewsw.github.io/portfolio/\">HAYLIEWSW.GITHUB.IO/PORTFOLIO/</link>",
        styles["Role"],
    ),
    Paragraph("PROFILE", styles["Section"]),
    Paragraph(
        "Product designer with four years of UX/UI and digital product experience. I turn complex workflows, information, and interaction systems into clear, practical experiences.",
        styles["Body"],
    ),
    Paragraph("CORE SKILLS", styles["Section"]),
    Paragraph(
        "&bull; Product design &nbsp;&nbsp;&nbsp; &bull; UX/UI design &nbsp;&nbsp;&nbsp; &bull; Information architecture &nbsp;&nbsp;&nbsp; &bull; Workflow design<br/>"
        "&bull; Design systems &nbsp;&nbsp;&nbsp; &bull; Wireframes, flows & prototypes &nbsp;&nbsp;&nbsp; &bull; Responsive design<br/>"
        "&bull; Remote usability testing &nbsp;&nbsp;&nbsp; &bull; Production specifications &nbsp;&nbsp;&nbsp; &bull; Art direction & game UX",
        styles["Body"],
    ),
    Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]),
]

experience = [
    ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Lead art direction and game UX; collaborate with development from concepts through playtesting and iteration."),
    ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Develop clear client communication and handle confidential information with discretion."),
    ("2023 - 2024", "Executive Assistant", "ed&c | Singapore", "Supported operational coordination and day-to-day organizational workflows."),
    ("2020 - 2022", "Digital Product Designer", "abillion | Singapore", "Led UX for a launched profile revamp: systems, flows, prototypes, specifications, and remote testing."),
    ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Designed responsive UI, flows, prototypes, and build-ready specifications for regional digital experiences."),
]

for entry in experience:
    story.append(two_column_entry(*entry))

story.append(Paragraph("SELECTED PROJECTS", styles["Section"]))
projects = [
    ("01", "Inventory Management System", "INDEPENDENT | PRODUCT DESIGN | OPERATIONS", "Built a Flask website that turns CSV and Notion data into a searchable inventory system."),
    ("02", "abillion Profile Revamp", "UX/UI | RESEARCH", "Sole UX designer for a launched profile feature; tested in UXArmy with four participants across eight tasks."),
    ("03", "Mad John", "GAME UX | ART DIRECTION", "Six mixed-experience playtesters informed a hands-on tutorial and ongoing scoring refinement."),
    ("04", "Sompo Asia Website Revamp", "RESPONSIVE UI | INFORMATION ARCHITECTURE", "Designed desktop and mobile UI, states, flows, prototypes, and production specifications for a two-month launch."),
    ("05", "Toadally In Love", "GAME JAM | ART DIRECTION | UX", "Led a four-day build ranked third overall among 73 entries, including second for gameplay and audio."),
]

project_rows = []
for number, title, meta, description in projects:
    content = [Paragraph(title, styles["Job"]), Paragraph(meta, styles["ProjectMeta"]), Paragraph(description, styles["Body"])]
    project_rows.append([Paragraph(number, styles["ProjectNumber"]), content])

project_table = Table(project_rows, colWidths=[.42 * inch, 6.53 * inch])
project_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 1),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
]))
story += [project_table, Paragraph("EDUCATION", styles["Section"])]

education = [
    ("2022 - 2023", "Design Management (Post-graduate Certificate)", "George Brown College | Toronto, Canada", "Dean’s List: Fall 2022 and Winter 2023."),
    ("2016 - 2017", "Bachelor of Communication (Professional Communications)", "RMIT University | Singapore & Australia", ""),
]

for date, title, school, note in education:
    content = [Paragraph(title, styles["Job"]), Paragraph(school, styles["Company"])]
    if note:
        content.append(Paragraph(note, styles["Body"]))
    table = Table([[Paragraph(date, styles["Date"]), content]], colWidths=[.85 * inch, 6.1 * inch])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(KeepTogether(table))

document.build(story)
