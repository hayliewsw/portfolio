from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_JUSTIFY
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
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=27, leading=28, textColor=ink, spaceAfter=4))
styles.add(ParagraphStyle(name="Role", fontName="Helvetica", fontSize=8.2, leading=10.4, textColor=ink, spaceAfter=4))
styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=11.4, leading=13, textColor=ink, spaceBefore=4, spaceAfter=2, uppercase=True))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=8.1, leading=10.1, textColor=ink, spaceAfter=2))
styles.add(ParagraphStyle(name="Profile", parent=styles["Body"], alignment=TA_JUSTIFY, spaceAfter=2))
styles.add(ParagraphStyle(name="Job", fontName="Helvetica-Bold", fontSize=9.3, leading=10.8, textColor=ink, spaceAfter=1))
styles.add(ParagraphStyle(name="Company", fontName="Helvetica", fontSize=8.0, leading=9.6, textColor=ink, spaceAfter=1))
styles.add(ParagraphStyle(name="Date", fontName="Helvetica", fontSize=8.0, leading=9.6, textColor=ink))
styles.add(ParagraphStyle(name="ProjectNumber", fontName="Helvetica", fontSize=8.0, leading=9.6, textColor=ink))
styles.add(ParagraphStyle(name="ProjectMeta", fontName="Helvetica-Bold", fontSize=7.2, leading=8.7, textColor=ink, spaceAfter=1))


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
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return KeepTogether(table)


story = [
    Paragraph("HAYLIE WONG", styles["Name"]),
    Paragraph(
        "<b>PRODUCT DESIGNER</b><br/>"
        "TORONTO, ON<br/>"
        "<link href=\"mailto:hayliewsw@gmail.com\">hayliewsw@gmail.com</link> | "
        "<link href=\"https://www.linkedin.com/in/hayliewsw/\">linkedin.com/in/hayliewsw</link> | "
        "<link href=\"https://hayliewsw.github.io/portfolio/\">hayliewsw.github.io/portfolio/</link>",
        styles["Role"],
    ),
    Paragraph("PROFILE", styles["Section"]),
    Paragraph(
        "Digital product designer with four years of UX/UI and product experience across mobile, responsive web, and game UX. I turn complex workflows, information, and interaction systems into clear, practical experiences. My end-to-end practice spans research, information architecture, user flows, prototypes, interface systems, production specifications, and usability testing. I collaborate closely with stakeholders and developers to translate operational needs into dependable customer journeys.",
        styles["Profile"],
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
    ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Co-founded a game studio; lead art direction and game UX from concepts through playtesting, partnering with development to iterate gameplay."),
    ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote", "Design and playtest small game projects, shaping interaction flows, visual systems, onboarding, and moment-to-moment feedback alongside development collaborators."),
    ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Write clear, audience-aware immigration content while handling sensitive client information with discretion and accuracy."),
    ("2023 - 2024", "Executive Assistant", "ed&c | Singapore", "Coordinated priorities and operational workflows, keeping day-to-day work organized and stakeholders aligned."),
    ("2020 - 2022", "Digital Product Designer", "abillion | Singapore", "Owned end-to-end UX for a launched profile revamp, delivering systems, flows, prototypes, specifications, and remote usability testing."),
    ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Designed responsive website experiences, translating brand and information-architecture needs into UI, prototypes, and build-ready specifications."),
]

for entry in experience:
    story.append(two_column_entry(*entry))

story.append(Paragraph("SELECTED PROJECTS", styles["Section"]))
projects = [
    ("01", "Inventory Management System", "INDEPENDENT | PRODUCT DESIGN | OPERATIONS", "Independently designed and built a searchable inventory website in five days, turning CSV and Notion data into categories, filters, and location-aware views."),
    ("02", "abillion Profile Revamp", "UX/UI | RESEARCH", "Sole UX designer for a launched profile revamp, defining systems, flows, prototypes, and specifications; validated in UXArmy with four participants across eight tasks."),
    ("03", "Mad John", "GAME UX | ART DIRECTION", "Co-created an in-progress card-and-puzzle game; led game UX and art direction, using six mixed-experience playtests to introduce a hands-on tutorial and refine scoring."),
    ("04", "Sompo Asia Website Revamp", "RESPONSIVE UI | INFORMATION ARCHITECTURE", "Designed a full regional website across desktop and mobile, translating a refreshed brand and clearer information architecture into flows, states, and specifications. <link href=\"https://www.sompo-apac.com/\">View the live website</link>."),
    ("05", "Toadally In Love", "GAME JAM | ART DIRECTION | UX", "Led art direction and UX for a four-day puzzle-game build, creating a readable interaction system and visual world that ranked third overall among 73 entries. <link href=\"https://szzzeler.itch.io/toadally-in-love\">Play on itch.io</link>."),
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
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
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
