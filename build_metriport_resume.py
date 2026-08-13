from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Table, TableStyle


OUTPUT = Path("output/pdf/Haylie-Wong-Metriport-Product-Designer-Resume.pdf")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

INK = HexColor("#15201E")
GREEN = HexColor("#2B6A58")
MUTED = HexColor("#52615D")
LINE = HexColor("#CAD5D0")

doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=letter,
    leftMargin=.62 * inch,
    rightMargin=.62 * inch,
    topMargin=.34 * inch,
    bottomMargin=.27 * inch,
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=25, leading=27, textColor=INK, spaceAfter=2))
styles.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=7.8, leading=9.5, textColor=INK, spaceAfter=2))
styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=10.7, leading=12, textColor=GREEN, spaceBefore=5, spaceAfter=2))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=7.8, leading=9.35, textColor=INK, spaceAfter=1.5))
styles.add(ParagraphStyle(name="Summary", parent=styles["Body"], fontSize=8.1, leading=9.9))
styles.add(ParagraphStyle(name="Role", fontName="Helvetica-Bold", fontSize=8.9, leading=10.1, textColor=INK, spaceAfter=.5))
styles.add(ParagraphStyle(name="Meta", fontName="Helvetica", fontSize=7.4, leading=8.7, textColor=MUTED, spaceAfter=1))
styles.add(ParagraphStyle(name="Date", fontName="Helvetica-Bold", fontSize=7.3, leading=9, textColor=GREEN))
styles.add(ParagraphStyle(name="ProjectMeta", fontName="Helvetica-Bold", fontSize=7.1, leading=8.4, textColor=GREEN, spaceAfter=.6))


def link(url, label):
    return f'<link href="{url}" color="#2B6A58"><u>{label}</u></link>'


def row(date, title, org, body):
    content = [Paragraph(title, styles["Role"]), Paragraph(org, styles["Meta"]), Paragraph(body, styles["Body"])]
    table = Table([[Paragraph(date, styles["Date"]), content]], colWidths=[.9 * inch, 6.05 * inch])
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
    Paragraph("PRODUCT DESIGNER | COMPLEX WORKFLOWS | SYSTEMS + INTERACTION DESIGN", styles["Contact"]),
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
        "Product designer with four years of UX/UI and product experience across operational tools, mobile products, and responsive web. I take ambiguous problems from customer and stakeholder discovery through flows, systems, prototypes, specifications, testing, and delivery. My approach balances speed with durable design decisions: clarify the workflow, make the product tangible early, and collaborate closely with engineers to ship a considered result.",
        styles["Summary"],
    ),
    Paragraph("CORE CAPABILITIES", styles["Section"]),
    Paragraph(
        "End-to-end product design  |  Complex workflow design  |  Design systems and reusable components  |  Information architecture<br/>"
        "Figma  |  Responsive UI  |  Prototypes and interaction flows  |  Production specifications  |  Usability testing  |  Brand and visual design<br/>"
        "Cross-functional collaboration  |  AI-assisted prototyping  |  GitHub workflows  |  HTML/CSS familiarity",
        styles["Body"],
    ),
    Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]),
]

experience = [
    ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Co-founded an independent game studio and own art direction and game UX from concept through playtesting. Set the visual direction, define interaction and onboarding patterns, and partner directly with development to turn feedback into product improvements."),
    ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote", "Originate and prototype interactive products using Figma, Godot, GitHub, and AI-assisted coding. Balance fast v0 exploration with visual-system decisions, clear gameplay feedback, and iterative testing alongside development collaborators."),
    ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Translate complex, high-stakes information into accurate, audience-aware guidance, bringing clarity and careful judgment to customer-facing communication."),
    ("2023 - 2024", "Executive Assistant", "ed&c | Singapore", "Coordinated executive priorities, communications, and operational workflows while keeping confidential work organized and stakeholders aligned."),
    ("2020 - 2022", "Digital Product Designer", "abillion | Singapore", "Owned end-to-end UX for a launched profile revamp across personal, social, collection, settings, empty, error, and offline states. Created reusable patterns, flows, prototypes, and build-ready specifications; partnered across product, engineering, marketing, and data and validated the direction through moderated usability testing."),
    ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Designed responsive digital experiences from information architecture through production-ready UI. Translated client brands and complex content into coherent page systems while collaborating with project managers, client stakeholders, and developers through delivery."),
]

for item in experience:
    story.append(row(*item))

story.append(Paragraph("SELECTED PRODUCT WORK", styles["Section"]))

projects = [
    ("01", "Inventory Management System", "INDEPENDENT | OPERATIONAL WORKFLOWS | 5-DAY BUILD", "Identified, designed, built, and iterated a working inventory website in five days. Turned CSV and Notion data into clear categories, filters, and location-aware stock and sales views, demonstrating rapid scoping, information architecture, and hands-on execution."),
    ("02", "abillion Profile Revamp", "SHIPPED MOBILE PRODUCT | SYSTEMS | RESEARCH", "Sole UX designer for a launched profile redesign. Defined the end-to-end state system and production specifications, then ran eight moderated tasks with four participants to identify friction and refine the hierarchy before release."),
    ("03", "Sompo Asia Website Revamp", "RESPONSIVE SYSTEM | BRAND | ENGINEERING HANDOFF", "Designed a complete regional website across desktop and mobile in a two-month engagement, translating a refreshed brand and complex information architecture into reusable page patterns, responsive states, prototypes, and build-ready specifications. " + link("https://www.sompo-apac.com/", "Live website") + "."),
]

project_rows = []
for number, title, meta, body in projects:
    project_rows.append([
        Paragraph(number, styles["Date"]),
        [Paragraph(title, styles["Role"]), Paragraph(meta, styles["ProjectMeta"]), Paragraph(body, styles["Body"])],
    ])

project_table = Table(project_rows, colWidths=[.42 * inch, 6.53 * inch])
project_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 1),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
]))
story.append(project_table)

story.append(Paragraph("EDUCATION", styles["Section"]))
story.append(row("2022 - 2023", "Design Management, Post-graduate Certificate", "George Brown College | Toronto, Canada", "Dean's List: Fall 2022 and Winter 2023."))
story.append(row("2016 - 2017", "Bachelor of Communication, Professional Communications", "RMIT University | Singapore & Australia", ""))

doc.build(story)
print(OUTPUT)
