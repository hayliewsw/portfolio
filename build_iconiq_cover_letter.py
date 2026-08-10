from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


output_path = Path("output/pdf/Haylie-Wong-ICONIQ-Cover-Letter.pdf")
output_path.parent.mkdir(parents=True, exist_ok=True)

ink = HexColor("#000000")
document = SimpleDocTemplate(
    str(output_path),
    pagesize=letter,
    rightMargin=.82 * inch,
    leftMargin=.82 * inch,
    topMargin=.72 * inch,
    bottomMargin=.72 * inch,
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=21, leading=24, textColor=ink, spaceAfter=4))
styles.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=9, leading=12, textColor=ink, spaceAfter=18))
styles.add(ParagraphStyle(name="Letter", fontName="Helvetica", fontSize=10.4, leading=15.4, textColor=ink, spaceAfter=13))

story = [
    Paragraph("HAYLIE WONG", styles["Name"]),
    Paragraph(
        "Relocating to San Francisco, CA | Housing secured<br/>"
        "hayliewsw@gmail.com | linkedin.com/in/hayliewsw | hayliewsw.github.io/portfolio/",
        styles["Contact"],
    ),
    Paragraph("Dear ICONIQ Hiring Team,", styles["Letter"]),
    Paragraph(
        "I am excited to apply for the Office Coordinator role at ICONIQ. I am drawn to work that creates a welcoming, well-run environment for people to do their best work. With experience supporting executive priorities, coordinating daily operations, and communicating with care and discretion, I would bring a calm, proactive approach to the San Francisco office.",
        styles["Letter"],
    ),
    Paragraph(
        "As an Executive Assistant at ed&amp;c, I coordinated priorities, schedules, communications, and operational workflows while keeping stakeholders aligned. In my current role as Senior Copywriter at The Immigration People, I work with confidential client information and communicate clearly in high-trust situations. Across both roles, I have developed the organization, responsiveness, and attention to detail needed to keep moving pieces on track and make every interaction feel considered.",
        styles["Letter"],
    ),
    Paragraph(
        "I also bring a product-design background that strengthens my ability to notice friction, organize information, and improve everyday workflows. I enjoy anticipating needs, creating simple systems, and partnering across teams to solve practical problems before they become disruptions. I would be comfortable supporting guests, conference-room readiness, vendors, supplies, onboarding, and the many details that contribute to a polished office experience.",
        styles["Letter"],
    ),
    Paragraph(
        "I am relocating to San Francisco with housing secured and am seeking employer-sponsored U.S. work authorization. Thank you for considering my application. I would welcome the opportunity to discuss how my operational experience, service mindset, and thoughtful approach could support ICONIQ's team.",
        styles["Letter"],
    ),
    Spacer(1, 6),
    Paragraph("Sincerely,<br/>Haylie Wong", styles["Letter"]),
]

document.build(story)
