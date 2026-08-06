from pathlib import Path
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

output_path = Path("output/pdf/Haylie-Wong-Resume.pdf")
output_path.parent.mkdir(parents=True, exist_ok=True)
ink, accent = HexColor("#090909"), HexColor("#FF4D2E")
document = SimpleDocTemplate(str(output_path), pagesize=letter, rightMargin=.7*inch, leftMargin=.7*inch, topMargin=.55*inch, bottomMargin=.5*inch)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=29, leading=29, textColor=ink, spaceAfter=5))
styles.add(ParagraphStyle(name="Role", fontName="Helvetica", fontSize=8.4, leading=12, textColor=ink, spaceAfter=14))
styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=7.5, leading=9, textColor=accent, spaceBefore=10, spaceAfter=5, uppercase=True))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=8.6, leading=11.6, textColor=ink, spaceAfter=4))
styles.add(ParagraphStyle(name="Job", fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=ink, spaceAfter=2))
styles.add(ParagraphStyle(name="Date", fontName="Helvetica", fontSize=7.7, leading=10, textColor=ink))

story = [Paragraph("HAYLIE WONG", styles["Name"]), Paragraph("PRODUCT DESIGNER | TORONTO, ON | HAYLIEWSW@GMAIL.COM | LINKEDIN.COM/IN/HAYLIEWSW", styles["Role"]), Paragraph("PROFILE", styles["Section"]), Paragraph("Product designer with four years of dedicated UX/UI and digital product experience. I bring a communication-first approach to complex information, practical workflows, visual craft, and cross-functional collaboration.", styles["Body"]), Paragraph("EXPERIENCE", styles["Section"])]
experience = [("2026 - Present", "Co-founder | Oupelaye Studio | Quebec, Canada", "Co-founding a game studio. Lead art direction and game UX while collaborating closely with development."), ("2023 - Present", "Senior Copywriter | The Immigration People | Singapore", "Develop clear communication while handling clients’ confidential information with discretion."), ("2023 - 2024", "Executive Assistant | ed&c | Singapore", "Supported organizational operations and day-to-day coordination."), ("2020 - 2022", "Digital Product Designer | Abiilion | Singapore", "Contributed UX/UI and digital product design work in cross-team collaboration."), ("2017 - 2019", "UX/UI Designer | Decision Science | Singapore", "Worked across UI design and UX research.")]
for date, title, description in experience:
    content = [Paragraph(title, styles["Job"]), Paragraph(description, styles["Body"])]
    table = Table([[Paragraph(date, styles["Date"]), content]], colWidths=[1.25*inch, 5.7*inch])
    table.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("BOTTOMPADDING", (0,0), (-1,-1), 7)]))
    story.append(KeepTogether(table))
story += [Paragraph("SELECTED PROJECT", styles["Section"]), Paragraph("Inventory Management System — Designed and built a user-friendly website from a CSV database to organize inventory records, stock availability, sales, and movement. Structured listing, storage, and fulfillment documentation through a more intuitive inventory interface.", styles["Body"]), Paragraph("EDUCATION", styles["Section"]), Paragraph("Design Management, Post-graduate Certificate — George Brown College, Toronto, Canada (2022–2023). Dean’s List: Fall 2022, Winter 2023.", styles["Body"]), Paragraph("Bachelor of Communication, Professional Communications — RMIT University, Singapore & Australia (2016–2017).", styles["Body"])]
document.build(story)
