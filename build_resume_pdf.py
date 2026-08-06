from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

output_path = Path("output/pdf/Haylie-Wong-Resume.pdf")
output_path.parent.mkdir(parents=True, exist_ok=True)
ink = HexColor("#1C2632")
accent = HexColor("#E6533C")

document = SimpleDocTemplate(str(output_path), pagesize=letter, rightMargin=.7 * inch, leftMargin=.7 * inch, topMargin=.62 * inch, bottomMargin=.55 * inch)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=31, leading=31, textColor=ink, spaceAfter=7))
styles.add(ParagraphStyle(name="Role", fontName="Helvetica", fontSize=11, leading=15, textColor=ink, spaceAfter=20))
styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=accent, spaceBefore=14, spaceAfter=7, uppercase=True, tracking=1.1))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=9.4, leading=14, textColor=ink, spaceAfter=6))
styles.add(ParagraphStyle(name="Job", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=ink, spaceAfter=3))
styles.add(ParagraphStyle(name="Date", fontName="Helvetica", fontSize=8.4, leading=12, textColor=ink))
styles.add(ParagraphStyle(name="ResumeBullet", fontName="Helvetica", fontSize=8.7, leading=12.5, textColor=ink, leftIndent=10, firstLineIndent=-8, spaceAfter=2))

story = [Paragraph("HAYLIE WONG", styles["Name"]), Paragraph("PRODUCT DESIGNER &nbsp; | &nbsp; TORONTO, ON &nbsp; | &nbsp; HAYLIEWSW@GMAIL.COM &nbsp; | &nbsp; LINKEDIN.COM/IN/HAYLIEWSW", styles["Role"]), Paragraph("PROFILE", styles["Section"]), Paragraph("Product designer with 5 years of experience turning complex needs into clear flows, polished interfaces, and practical design systems. I balance customer insight, business context, and technical constraints to help teams ship experiences that are easy to use and built to last.", styles["Body"]), Paragraph("EXPERIENCE", styles["Section"])]

experience = [("2021 - Present", "Product Designer | Digital Products", "Lead end-to-end product design across discovery, flows, interaction design, prototyping, and high-fidelity UI. Partner with product and engineering teams to clarify problems, align on solutions, and evolve experiences through feedback.", ["Translate customer and business needs into clear, accessible user journeys.", "Create wireframes, prototypes, and production-ready interfaces in Figma.", "Build reusable patterns that improve consistency and speed across product surfaces."]), ("2024 - Present", "Indie Game Developer | Interactive Experiences", "Design and build an original interactive product from concept to playable experience, with a focus on onboarding, feedback loops, progression, and player delight.", ["Define interaction systems and UI that make complex objectives easy to understand.", "Iterate on flows and moments of friction through playtesting and observation."])]

for date, title, description, bullets in experience:
    content = [Paragraph(title, styles["Job"]), Paragraph(description, styles["Body"])]
    content.extend(Paragraph(f"• {bullet}", styles["ResumeBullet"]) for bullet in bullets)
    table = Table([[Paragraph(date, styles["Date"]), content]], colWidths=[1.25 * inch, 5.7 * inch])
    table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOTTOMPADDING", (0, 0), (-1, -1), 14)]))
    story.append(KeepTogether(table))

story += [Paragraph("CAPABILITIES", styles["Section"]), Table([[Paragraph("Product strategy<br/>UX & interaction design<br/>UI & visual craft<br/>Prototyping & testing", styles["Body"]), Paragraph("Design systems<br/>Information architecture<br/>Cross-functional collaboration<br/>HTML & CSS fluency", styles["Body"]), Paragraph("Figma · FigJam<br/>Adobe Creative Suite<br/>Product analytics<br/>Agile product delivery", styles["Body"])]], colWidths=[2.3 * inch, 2.4 * inch, 2.25 * inch]), Spacer(1, 18), Paragraph("Available for thoughtful product design opportunities.", styles["Body"])]
document.build(story)
