from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Table, TableStyle


OUT = Path("output/pdf")
OUT.mkdir(parents=True, exist_ok=True)

INK = HexColor("#1B1A24")
MUTED = HexColor("#625E70")
PURPLE = HexColor("#6844C8")
LINE = HexColor("#D9D3E8")


def link(url, label):
    return f'<link href="{url}" color="#6844C8"><u>{label}</u></link>'


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
    path = OUT / "Haylie-Wong-Tilt-Senior-Copywriter-Brand-Resume.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=letter,
        leftMargin=.62 * inch, rightMargin=.62 * inch,
        topMargin=.35 * inch, bottomMargin=.28 * inch,
        title="Haylie Wong - Senior Copywriter, Brand Resume",
        author="Haylie Wong",
        subject="Application for Senior Copywriter, Brand at Tilt",
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=25, leading=27, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Tag", fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=PURPLE, spaceAfter=2))
    styles.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=7.75, leading=9.4, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=10.3, leading=11.8, textColor=PURPLE, spaceBefore=5, spaceAfter=2))
    styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=7.65, leading=9.2, textColor=INK, spaceAfter=1.4))
    styles.add(ParagraphStyle(name="Summary", parent=styles["Body"], fontSize=8, leading=9.7))
    styles.add(ParagraphStyle(name="Role", fontName="Helvetica-Bold", fontSize=8.65, leading=9.9, textColor=INK, spaceAfter=.4))
    styles.add(ParagraphStyle(name="Meta", fontName="Helvetica", fontSize=7.3, leading=8.5, textColor=MUTED, spaceAfter=.9))
    styles.add(ParagraphStyle(name="Date", fontName="Helvetica-Bold", fontSize=7.2, leading=8.8, textColor=PURPLE))

    story = [
        Paragraph("HAYLIE WONG", styles["Name"]),
        Paragraph("SENIOR COPYWRITER | BRAND STORYTELLING | AI-ASSISTED CREATION", styles["Tag"]),
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
            "Senior copywriter, product thinker, and visual collaborator who turns complex, consequential subjects into clear, human, audience-aware stories. I combine professional writing with four years of digital product design, bringing language, visual systems, and customer journeys together rather than treating copy as a final layer. My practice spans long- and short-form writing, narrative development, content hierarchy, customer research, art direction, and AI-assisted workflows grounded in human judgment and craft.",
            styles["Summary"],
        ),
        Paragraph("CORE CAPABILITIES", styles["Section"]),
        Paragraph(
            "Brand voice & narrative development  |  Long- and short-form copy  |  Plain-language communication<br/>"
            "Campaign concepting  |  Product and customer storytelling  |  Content hierarchy  |  Audience research<br/>"
            "Creative collaboration  |  Visual storytelling  |  Figma  |  Style systems & documentation  |  AI-assisted ideation and workflows",
            styles["Body"],
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]),
    ]

    entries = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada",
         "Shape the studio's creative identity, product story, and player experience. Lead art direction and game UX from concept through playtesting, partnering with development to turn narrative, visual, and interaction ideas into a coherent experience."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote",
         "Develop original concepts through narrative framing, visual storytelling, AI-assisted prototyping, interaction design, and iterative playtesting. Use Figma, Godot, GitHub, and generative tools to move quickly from an idea to something audiences can experience and respond to."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore",
         "Translate complex, high-stakes immigration topics into clear, useful, audience-aware guidance. Adapt voice, structure, and detail to customer needs while maintaining accuracy, discretion, and consistency across sensitive communications."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore",
         "Owned end-to-end UX for a shipped profile revamp, translating customer insight into clearer information hierarchy, product direction, prototypes, and launch-ready experiences. Collaborated across product, engineering, marketing, and data and conducted moderated usability research."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore",
         "Translated client brands, business goals, and complex information into responsive web experiences and narrative page structures. Developed visual systems, prototypes, and production specifications in partnership with clients, project managers, and developers."),
    ]

    for date, role, org, body in entries:
        details = [Paragraph(role, styles["Role"]), Paragraph(org, styles["Meta"]), Paragraph(body, styles["Body"])]
        story.append(KeepTogether(table_no_padding([[Paragraph(date, styles["Date"]), details]], [.9 * inch, 6.05 * inch])))

    story += [Paragraph("SELECTED CREATIVE WORK", styles["Section"])]
    projects = [
        ("Content + Product Storytelling Portfolio",
         "Developed original long-form, social, and customer-story concepts demonstrating range across narrative writing, campaign extension, audience insight, and visual communication."),
        ("abillion Profile Revamp | Customer-Led Product Storytelling",
         "Led a shipped redesign and an eight-task moderated study with four participants, translating customer friction into a clearer content and interaction system."),
        ("Sompo Asia Website Revamp | Brand Translation",
         "Translated a refreshed regional brand and complex information architecture into a cohesive responsive website across desktop and mobile."),
        ("Toadally In Love | Narrative, Art Direction & UX",
         "Led art direction and UX for a four-day puzzle-game build, creating a distinct visual world and readable interaction language that ranked third overall among 73 entries."),
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
