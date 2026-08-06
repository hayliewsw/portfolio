from pathlib import Path
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

output_path = Path("output/pdf/Haylie-Wong-Resume.pdf")
output_path.parent.mkdir(parents=True, exist_ok=True)
ink, accent = HexColor("#000000"), HexColor("#000000")
document = SimpleDocTemplate(str(output_path), pagesize=letter, rightMargin=.7*inch, leftMargin=.7*inch, topMargin=.28*inch, bottomMargin=.28*inch)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=27, leading=27, textColor=ink, spaceAfter=6))
styles.add(ParagraphStyle(name="Role", fontName="Helvetica", fontSize=8.5, leading=11.5, textColor=ink, spaceAfter=13))
styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=13, leading=15, textColor=accent, spaceBefore=10, spaceAfter=5, uppercase=True))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=8.5, leading=11.3, textColor=ink, spaceAfter=4))
styles.add(ParagraphStyle(name="Job", fontName="Helvetica-Bold", fontSize=9.6, leading=11.5, textColor=ink, spaceAfter=2))
styles.add(ParagraphStyle(name="Company", fontName="Helvetica", fontSize=8.4, leading=10, textColor=ink, spaceAfter=2))
styles.add(ParagraphStyle(name="Date", fontName="Helvetica", fontSize=8.4, leading=10, textColor=ink))
styles.add(ParagraphStyle(name="ProjectNumber", fontName="Helvetica", fontSize=8.4, leading=10, textColor=ink))
styles.add(ParagraphStyle(name="ProjectMeta", fontName="Helvetica-Bold", fontSize=7.6, leading=9.5, textColor=ink, spaceAfter=2))

story = [Paragraph("HAYLIE WONG", styles["Name"]), Paragraph("<b>PRODUCT DESIGNER</b><br/>TORONTO, ON | <link href=\"mailto:hayliewsw@gmail.com\">HAYLIEWSW@GMAIL.COM</link> | <link href=\"https://www.linkedin.com/in/hayliewsw/\">LINKEDIN.COM/IN/HAYLIEWSW</link>", styles["Role"]), Paragraph("PROFILE", styles["Section"]), Paragraph("Product designer with four years of dedicated UX/UI and digital product experience. I bring a communication-first approach to complex information, practical workflows, visual craft, and cross-functional collaboration.", styles["Body"]), Paragraph("CORE SKILLS", styles["Section"]), Paragraph("&bull; Product design &nbsp;&nbsp;&nbsp; &bull; UX/UI design &nbsp;&nbsp;&nbsp; &bull; Information architecture<br/>&bull; Workflow design &nbsp;&nbsp;&nbsp; &bull; UX research &nbsp;&nbsp;&nbsp; &bull; Visual design<br/>&bull; Cross-team collaboration &nbsp;&nbsp;&nbsp; &bull; Art direction &nbsp;&nbsp;&nbsp; &bull; Game UX", styles["Body"]), Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"])]
experience = [("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Co-founding a game studio. Lead art direction and game UX while collaborating closely with development."), ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Develop clear communication while handling clients’ confidential information with discretion."), ("2023 - 2024", "Executive Assistant", "ed&c | Singapore", "Supported organizational operations and day-to-day coordination."), ("2020 - 2022", "Digital Product Designer", "abiilion | Singapore", "Contributed UX/UI and digital product design work in cross-team collaboration."), ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Worked across UI design and UX research.")]
for date, title, company, description in experience:
    content = [Paragraph(title, styles["Job"]), Paragraph(company, styles["Company"]), Paragraph(description, styles["Body"])]
    table = Table([[Paragraph(date, styles["Date"]), content]], colWidths=[.85*inch, 6.1*inch])
    table.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (0,-1), 0), ("BOTTOMPADDING", (0,0), (-1,-1), 4)]))
    story.append(KeepTogether(table))
story.append(Paragraph("SELECTED PROJECTS", styles["Section"]))
projects = [
    ("01", "Inventory Management System", "Independent project | Product design | Operations", "Turning a CSV database into a clearer, more useful operational workflow."),
    ("02", "Product Design at Abiilion", "Digital product design | UX/UI", "Contributing to digital product work through cross-team collaboration."),
    ("03", "Oupelaye Studio", "Game UX | Art direction", "Co-founding a game studio and shaping its art direction and player experience."),
]
project_rows = []
for number, title, meta, description in projects:
    content = [Paragraph(title, styles["Job"]), Paragraph(meta.upper(), styles["ProjectMeta"]), Paragraph(description, styles["Body"])]
    project_rows.append([Paragraph(number, styles["ProjectNumber"]), content])
project_table = Table(project_rows, colWidths=[.42*inch, 6.53*inch])
project_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
story += [project_table, Paragraph("EDUCATION", styles["Section"])]
education = [("2022 - 2023", "Design Management (Post-graduate Certificate)", "George Brown College | Toronto, Canada", "Dean’s List: Fall 2022 and Winter 2023."), ("2016 - 2017", "Bachelor of Communication (Professional Communications)", "RMIT University | Singapore & Australia", "")]
for date, title, school, note in education:
    content = [Paragraph(title, styles["Job"]), Paragraph(school, styles["Company"])]
    if note:
        content.append(Paragraph(note, styles["Body"]))
    table = Table([[Paragraph(date, styles["Date"]), content]], colWidths=[.85*inch, 6.1*inch])
    table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (0, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    story.append(KeepTogether(table))
document.build(story)
