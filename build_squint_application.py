from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUT = Path("output/pdf")
OUT.mkdir(parents=True, exist_ok=True)

INK = HexColor("#17211F")
MUTED = HexColor("#52615D")
GREEN = HexColor("#2E6B57")
PALE = HexColor("#EAF2ED")
ORANGE = HexColor("#E86E3A")
CREAM = HexColor("#F8F5EE")
LINE = HexColor("#CAD5D0")


def link(url, label):
    return f'<link href="{url}" color="#2E6B57"><u>{label}</u></link>'


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


def build_resume():
    path = OUT / "Haylie-Wong-Squint-Content-Marketing-Lead-Resume.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=letter,
        leftMargin=.62 * inch, rightMargin=.62 * inch,
        topMargin=.35 * inch, bottomMargin=.28 * inch,
    )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="RName", fontName="Helvetica-Bold", fontSize=25, leading=27, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="RContact", fontName="Helvetica", fontSize=7.8, leading=9.5, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="RSection", fontName="Helvetica-Bold", fontSize=10.5, leading=12, textColor=GREEN, spaceBefore=5, spaceAfter=2))
    styles.add(ParagraphStyle(name="RBody", fontName="Helvetica", fontSize=7.7, leading=9.25, textColor=INK, spaceAfter=1.5))
    styles.add(ParagraphStyle(name="RSummary", parent=styles["RBody"], fontSize=8, leading=9.8))
    styles.add(ParagraphStyle(name="RJob", fontName="Helvetica-Bold", fontSize=8.8, leading=10, textColor=INK, spaceAfter=.5))
    styles.add(ParagraphStyle(name="RMeta", fontName="Helvetica", fontSize=7.4, leading=8.7, textColor=MUTED, spaceAfter=1))
    styles.add(ParagraphStyle(name="RDate", fontName="Helvetica-Bold", fontSize=7.3, leading=9, textColor=GREEN))

    story = [
        Paragraph("HAYLIE WONG", styles["RName"]),
        Paragraph("CONTENT MARKETING | PRODUCT STORYTELLING | AI-ASSISTED CREATION", styles["RContact"]),
        Paragraph(
            "Relocating to San Francisco, CA | Housing secured | Requires employer-sponsored U.S. work authorization<br/>"
            "hayliewsw@gmail.com | "
            + link("https://www.linkedin.com/in/hayliewsw/", "linkedin.com/in/hayliewsw") + " | "
            + link("https://hayliewsw.github.io/portfolio/", "hayliewsw.github.io/portfolio"),
            styles["RContact"],
        ),
        HRFlowable(width="100%", thickness=.7, color=LINE, spaceBefore=2, spaceAfter=3),
        Paragraph("PROFILE", styles["RSection"]),
        Paragraph(
            "Writer, product thinker, and hands-on builder with senior copywriting experience and four years in digital product design. I turn complex products and customer needs into clear, audience-aware narratives, then extend those ideas through visual systems, prototypes, and content across formats. My work combines customer research, brand judgment, cross-functional collaboration, and AI-assisted execution in startup and client environments.",
            styles["RSummary"],
        ),
        Paragraph("CORE CAPABILITIES", styles["RSection"]),
        Paragraph(
            "Long- and short-form writing  |  Product and customer storytelling  |  Audience research  |  Executive-ready communications<br/>"
            "Content strategy  |  Visual storytelling  |  Figma  |  AI-assisted prototyping  |  Usability testing  |  Cross-functional delivery",
            styles["RBody"],
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", styles["RSection"]),
    ]

    entries = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Shape the studio's product story and player experience, leading art direction and game UX from concept through playtesting. Partner with development to turn qualitative feedback into clearer onboarding, product decisions, and visual communication."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote", "Develop and communicate original concepts through AI-assisted prototyping, interaction design, visual storytelling, and iterative playtesting. Use Figma, Godot, GitHub, and generative tools to move quickly from idea to tangible experience."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Create clear, audience-aware content that turns complex immigration topics into useful guidance. Adapt language to customer needs while maintaining accuracy, discretion, and a consistent voice across high-stakes communications."),
        ("2023 - 2024", "Executive Assistant", "ed&c | Singapore", "Produced and coordinated executive communications, priorities, and stakeholder updates across fast-moving operational work while handling confidential information with care."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore", "Owned end-to-end UX for a launched profile revamp. Partnered across product, engineering, marketing, and data; gathered customer insight through moderated research and translated findings into content hierarchy, product direction, prototypes, and launch-ready experiences."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Translated client brands, business goals, and complex information into responsive web experiences, narrative page structures, prototypes, and build-ready specifications with clients, project managers, and developers."),
    ]
    for date, title, org, body in entries:
        content = [Paragraph(title, styles["RJob"]), Paragraph(org, styles["RMeta"]), Paragraph(body, styles["RBody"])]
        story.append(KeepTogether(table_no_padding([[Paragraph(date, styles["RDate"]), content]], [.9 * inch, 6.05 * inch])))

    story += [Paragraph("SELECTED WORK", styles["RSection"])]
    projects = [
        ("Content + Product Storytelling Portfolio", "Original long-form, social, and customer-story concepts demonstrating range across writing, narrative development, and visual communication."),
        ("abillion Profile Revamp", "Led a shipped redesign and eight-task moderated study with four participants; synthesized customer friction into a clearer content and interaction system."),
        ("Inventory Management System", "Identified, designed, built, and iterated a working inventory website in five days, translating CSV and Notion data into clear operational views."),
    ]
    for title, body in projects:
        story.append(KeepTogether([Paragraph(title, styles["RJob"]), Paragraph(body, styles["RBody"])]))

    story += [
        Paragraph("EDUCATION", styles["RSection"]),
        table_no_padding([
            [Paragraph("2022 - 2023", styles["RDate"]), [Paragraph("Design Management, Post-graduate Certificate", styles["RJob"]), Paragraph("George Brown College | Dean's List", styles["RMeta"])]],
            [Paragraph("2016 - 2017", styles["RDate"]), [Paragraph("Bachelor of Communication, Professional Communications", styles["RJob"]), Paragraph("RMIT University | Singapore & Australia", styles["RMeta"])]],
        ], [.9 * inch, 6.05 * inch]),
    ]
    doc.build(story)
    return path


def portfolio_header(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.line(.62 * inch, .42 * inch, 7.88 * inch, .42 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(.62 * inch, .25 * inch, "HAYLIE WONG | CONTENT + PRODUCT STORYTELLING")
    canvas.drawRightString(7.88 * inch, .25 * inch, str(doc.page))
    canvas.restoreState()


def build_portfolio():
    path = OUT / "Haylie-Wong-Squint-Content-Portfolio.pdf"
    doc = SimpleDocTemplate(
        str(path), pagesize=letter,
        leftMargin=.72 * inch, rightMargin=.72 * inch,
        topMargin=.58 * inch, bottomMargin=.6 * inch,
    )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="PEyebrow", fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=ORANGE, spaceAfter=8))
    styles.add(ParagraphStyle(name="PTitle", fontName="Helvetica-Bold", fontSize=30, leading=33, textColor=INK, spaceAfter=12))
    styles.add(ParagraphStyle(name="PDeck", fontName="Helvetica", fontSize=13, leading=18, textColor=MUTED, spaceAfter=16))
    styles.add(ParagraphStyle(name="PH1", fontName="Helvetica-Bold", fontSize=22, leading=25, textColor=INK, spaceAfter=9))
    styles.add(ParagraphStyle(name="PH2", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=GREEN, spaceBefore=8, spaceAfter=5))
    styles.add(ParagraphStyle(name="PBody", fontName="Helvetica", fontSize=9.3, leading=13.3, textColor=INK, spaceAfter=8))
    styles.add(ParagraphStyle(name="PSmall", fontName="Helvetica", fontSize=7.8, leading=10.5, textColor=MUTED, spaceAfter=5))
    styles.add(ParagraphStyle(name="PQuote", fontName="Helvetica-Bold", fontSize=14, leading=19, textColor=GREEN, leftIndent=14, rightIndent=14, spaceBefore=8, spaceAfter=10))
    styles.add(ParagraphStyle(name="PNumber", fontName="Helvetica-Bold", fontSize=32, leading=34, textColor=ORANGE))
    styles.add(ParagraphStyle(name="PCenter", parent=styles["PDeck"], alignment=TA_CENTER))

    def pill(text_value):
        t = Table([[Paragraph(text_value, styles["PSmall"])]], colWidths=[2.05 * inch])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PALE),
            ("BOX", (0, 0), (-1, -1), .6, LINE),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        return t

    story = [
        Spacer(1, .55 * inch),
        Paragraph("CONTENT PORTFOLIO / 2026", styles["PEyebrow"]),
        Paragraph("Stories for the people who keep the physical world moving.", styles["PTitle"]),
        Paragraph("Long-form writing, social concepts, and customer storytelling created for Squint's Content Marketing Lead application.", styles["PDeck"]),
        Spacer(1, .12 * inch),
        Table([[pill("01  Narrative writing"), pill("02  Social series"), pill("03  Customer stories")]], colWidths=[2.2 * inch] * 3, style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ])),
        Spacer(1, .45 * inch),
        HRFlowable(width="100%", thickness=1, color=LINE, spaceAfter=14),
        Paragraph("THE THROUGHLINE", styles["PEyebrow"]),
        Paragraph("Technology earns attention when people can see themselves in the story.", styles["PH1"]),
        Paragraph("My approach starts with the audience: what they do, what slows them down, and what they need to trust. From there, I find the most concrete human tension, connect it to product value, and shape the story for the channel - without sanding away the specificity that makes it memorable.", styles["PBody"]),
        Spacer(1, .25 * inch),
        Paragraph("Haylie Wong", styles["PH2"]),
        Paragraph("Senior copywriter, product designer, and AI-assisted builder<br/>" + link("https://www.linkedin.com/in/hayliewsw/", "LinkedIn") + "  |  " + link("https://hayliewsw.github.io/portfolio/", "Product portfolio"), styles["PSmall"]),
        PageBreak(),

        Paragraph("01 / SPECULATIVE LONG-FORM", styles["PEyebrow"]),
        Paragraph("The most valuable machine in a factory might be the person standing beside it.", styles["PTitle"]),
        Paragraph("A narrative article concept for Squint about the knowledge hidden in everyday industrial work.", styles["PDeck"]),
        Paragraph("A line stops. Not dramatically - no sparks, no cinematic alarm - just a small change in sound that an experienced operator notices before anyone else. They tilt their head, listen again, and walk toward the machine. A few minutes later, production is moving.", styles["PBody"]),
        Paragraph("Ask what happened and the answer may sound almost too simple: <i>I've heard that noise before.</i>", styles["PQuote"]),
        Paragraph("That sentence contains years of pattern recognition. It holds the memory of previous failures, the feel of a healthy machine, the sequence of checks worth trying, and the judgment to know which warning can wait. None of it necessarily lives in a manual. Much of it lives in a person.", styles["PBody"]),
        Paragraph("Manufacturers often call this tribal knowledge. The phrase can make it sound informal or secondary, but on a factory floor it is operational infrastructure. It keeps lines moving, helps new operators avoid old mistakes, and turns written procedures into competent action. The problem is not that this knowledge is informal. The problem is that it is difficult to capture, difficult to find, and dangerously easy to lose.", styles["PBody"]),
        Paragraph("When expertise walks out the door", styles["PH2"]),
        Paragraph("An experienced worker does not leave behind only an empty role. They may take thousands of small decisions with them: which vibration matters, which workaround is safe, which step people consistently misread, and which question a new operator will be afraid to ask. Traditional documentation records the standard path. Experienced people often know what to do when reality refuses to follow it.", styles["PBody"]),
        Paragraph("The usual response is to document more. But a larger binder is not the same as accessible knowledge. Information can be technically available and still fail the person who needs it - buried in a shared drive, separated from the equipment, written without the context of the actual task, or frozen while the work keeps changing.", styles["PBody"]),
        Paragraph("The opportunity is not simply to store more information. It is to make operating knowledge usable at the moment of work.", styles["PQuote"]),
        PageBreak(),

        Paragraph("01 / SPECULATIVE LONG-FORM, CONTINUED", styles["PEyebrow"]),
        Paragraph("From documentation to intelligence", styles["PH1"]),
        Paragraph("Imagine if the operator hearing that unfamiliar noise could ask a question in plain language and receive guidance grounded in the organization's approved procedures, equipment context, and accumulated know-how. Imagine if the answer arrived where the work was happening, not after a search through disconnected systems.", styles["PBody"]),
        Paragraph("This is where industrial AI becomes meaningful. Its value is not that it sounds intelligent. Its value is that it can connect fragmented context and help a person take the next right action. The best system does not attempt to replace the operator's judgment; it makes more of the organization's knowledge available to that judgment.", styles["PBody"]),
        Paragraph("That distinction matters. Factory work is physical, contextual, and unforgiving of confident nonsense. Useful AI must be grounded in the standards, equipment, and reality of a specific organization. It should make expertise easier to access while keeping people in control of the work.", styles["PBody"]),
        Paragraph("Every operator an expert", styles["PH2"]),
        Paragraph("The phrase sounds ambitious because it is. Expertise still takes experience. But experience compounds faster when people can reach the right knowledge at the right moment - when a first-week operator can follow guidance shaped by a veteran, when a technician can surface the procedure that matches the machine in front of them, and when a manager can improve a workflow based on what actually happens on the floor.", styles["PBody"]),
        Paragraph("The knowledge gap in manufacturing is often described as a retirement problem. It is also a design problem. Critical knowledge exists, but the systems around it have not made that knowledge easy enough to capture, connect, and use.", styles["PBody"]),
        Paragraph("The next industrial revolution will not be powered by AI alone. It will be powered by the moment AI helps human expertise travel farther.", styles["PQuote"]),
        Spacer(1, .18 * inch),
        HRFlowable(width="100%", thickness=.7, color=LINE, spaceAfter=8),
        Paragraph("WHY THIS PIECE", styles["PEyebrow"]),
        Paragraph("I chose a human opening rather than a product opening. The article makes an abstract category - industrial intelligence - concrete through a recognizable moment, then moves from customer tension to Squint's product philosophy without reading like a feature list.", styles["PSmall"]),
        Paragraph("Disclosure: Speculative work created independently for this application. Product framing is based on Squint's publicly available website and job description; it was not commissioned or approved by Squint.", styles["PSmall"]),
        PageBreak(),

        Paragraph("02 / SPECULATIVE SOCIAL SERIES", styles["PEyebrow"]),
        Paragraph("One idea. Three ways into the feed.", styles["PTitle"]),
        Paragraph("A LinkedIn series designed to make industrial knowledge vivid, useful, and shareable.", styles["PDeck"]),
        Table([
            [Paragraph("01", styles["PNumber"]), [Paragraph("THE SOUND", styles["PH2"]), Paragraph("The machine did not send an alert.<br/><br/>It changed its sound.<br/><br/>The operator beside it noticed. She had heard that variation once before - three years ago, before a failure that stopped the line.<br/><br/>That is the challenge with tribal knowledge: it can prevent downtime, train the next generation, and protect quality. But too often, it lives in one person's memory.<br/><br/>Industrial AI becomes useful when it helps that expertise travel - to the next operator, the next shift, and the next site.", styles["PBody"])]],
            [Paragraph("02", styles["PNumber"]), [Paragraph("THE BINDER", styles["PH2"]), Paragraph("A 300-page procedure manual can contain the answer and still fail the person asking the question.<br/><br/>Because 'available' is not the same as accessible.<br/><br/>On the floor, the right information has to arrive:<br/>- in the context of the actual equipment<br/>- in language the operator can use<br/>- at the moment a decision is being made<br/><br/>The future of industrial knowledge is not a bigger binder. It is context that can act.", styles["PBody"])]],
            [Paragraph("03", styles["PNumber"]), [Paragraph("THE HANDOFF", styles["PH2"]), Paragraph("What does an expert leave behind when they retire?<br/><br/>Not just a job description.<br/><br/>They leave the workaround that saved a shift. The warning sound no manual describes. The question every new hire asks. The judgment that turns a procedure into a result.<br/><br/>Capturing that knowledge is not an archive project. It is how one generation of operators makes the next one stronger.", styles["PBody"])]],
        ], colWidths=[.55 * inch, 6.45 * inch], style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LINEBELOW", (0, 0), (-1, -2), .7, LINE),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ])),
        PageBreak(),

        Paragraph("03 / CUSTOMER STORY SYSTEM", styles["PEyebrow"]),
        Paragraph("Build the story from the floor up.", styles["PTitle"]),
        Paragraph("A repeatable interview-to-campaign system for turning customer outcomes into specific, credible narratives.", styles["PDeck"]),
        Table([
            [Paragraph("1", styles["PNumber"]), Paragraph("<b>Find the scene.</b><br/>Start with a specific shift, machine, worker, or failure - not a generic transformation claim.", styles["PBody"])],
            [Paragraph("2", styles["PNumber"]), Paragraph("<b>Follow the friction.</b><br/>Document the old workflow, where knowledge broke down, and what the consequences felt like for operators and managers.", styles["PBody"])],
            [Paragraph("3", styles["PNumber"]), Paragraph("<b>Earn the outcome.</b><br/>Connect measurable impact to the human behavior and product capability that produced it. Make every claim traceable.", styles["PBody"])],
            [Paragraph("4", styles["PNumber"]), Paragraph("<b>Design the series.</b><br/>Turn one interview into a flagship case study, executive post, operator quote card, short video, sales proof point, and follow-up lesson.", styles["PBody"])],
        ], colWidths=[.5 * inch, 6.5 * inch], style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BACKGROUND", (0, 0), (-1, -1), PALE),
            ("GRID", (0, 0), (-1, -1), .6, white),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ])),
        Spacer(1, .22 * inch),
        Paragraph("SAMPLE INTERVIEW PROMPTS", styles["PH2"]),
        Paragraph("- Take me to the moment you knew the old process was no longer working.<br/>- What did an experienced operator know that was difficult to teach or document?<br/>- What changed first after implementation: behavior, confidence, speed, or results?<br/>- Which outcome would sound impressive but miss the real reason this mattered?<br/>- What would another plant leader need to see before trusting this approach?", styles["PBody"]),
        Paragraph("WHY THIS SYSTEM", styles["PH2"]),
        Paragraph("The job is not simply to publish more. It is to create a dependable supply of differentiated stories. This system makes customer empathy operational: it protects specificity during interviews, connects human moments to business value, and creates multiple channel-ready assets from one strong source.", styles["PBody"]),
        PageBreak(),

        Paragraph("EXPERIENCE BEHIND THE WORK", styles["PEyebrow"]),
        Paragraph("Writing instinct, product rigor, and a builder's bias.", styles["PTitle"]),
        Paragraph("These speculative pieces are grounded in the way I already work across content and products.", styles["PDeck"]),
        Table([
            [Paragraph("SENIOR COPYWRITING", styles["PH2"]), Paragraph("At The Immigration People, I translate complex, high-stakes information into clear guidance while adapting voice and detail to the audience.", styles["PBody"])],
            [Paragraph("CUSTOMER UNDERSTANDING", styles["PH2"]), Paragraph("At abillion, I led moderated usability research across eight tasks, synthesized customer friction, and carried the findings into a launched product experience.", styles["PBody"])],
            [Paragraph("VISUAL RANGE", styles["PH2"]), Paragraph("My design background spans responsive websites, mobile products, information architecture, design systems, game UX, and art direction in Figma and production environments.", styles["PBody"])],
            [Paragraph("STARTUP AUTONOMY", styles["PH2"]), Paragraph("As a studio co-founder and independent creator, I originate concepts, make strategic and creative decisions, collaborate with development, and iterate directly from audience feedback.", styles["PBody"])],
            [Paragraph("AI-NATIVE EXECUTION", styles["PH2"]), Paragraph("I use AI for research synthesis, concept development, rapid prototyping, coding support, and iteration - then apply human judgment, testing, and craft to the output.", styles["PBody"])],
        ], colWidths=[1.62 * inch, 5.38 * inch], style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LINEBELOW", (0, 0), (-1, -2), .7, LINE),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ])),
        Spacer(1, .32 * inch),
        HRFlowable(width="100%", thickness=1, color=LINE, spaceAfter=14),
        Paragraph("LET'S MAKE INDUSTRIAL INTELLIGENCE IMPOSSIBLE TO IGNORE.", styles["PEyebrow"]),
        Paragraph("hayliewsw@gmail.com  |  " + link("https://www.linkedin.com/in/hayliewsw/", "LinkedIn") + "  |  " + link("https://hayliewsw.github.io/portfolio/", "Product portfolio"), styles["PBody"]),
    ]

    doc.build(story, onFirstPage=portfolio_header, onLaterPages=portfolio_header)
    return path


if __name__ == "__main__":
    print(build_resume())
    print(build_portfolio())
