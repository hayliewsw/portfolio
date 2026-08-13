import argparse
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Table, TableStyle


parser = argparse.ArgumentParser()
parser.add_argument(
    "--target",
    choices=["general", "bobyard", "iconiq", "ashby-designer", "ashby-support", "alhena", "rocket-operations", "mochi-pm", "sierra-designer"],
    default="general",
)
args = parser.parse_args()

is_bobyard = args.target == "bobyard"
is_iconiq = args.target == "iconiq"
is_ashby_designer = args.target == "ashby-designer"
is_ashby_support = args.target == "ashby-support"
is_alhena = args.target == "alhena"
is_rocket_operations = args.target == "rocket-operations"
is_mochi_pm = args.target == "mochi-pm"
is_sierra_designer = args.target == "sierra-designer"
output_path = Path(
    "output/pdf/Haylie-Wong-Sierra-Product-Designer-Resume.pdf"
    if is_sierra_designer
    else "output/pdf/Haylie-Wong-Mochi-Health-Product-Manager-Resume.pdf"
    if is_mochi_pm
    else "output/pdf/Haylie-Wong-Rocket-Money-Operations-Associate-Resume.pdf"
    if is_rocket_operations
    else "output/pdf/Haylie-Wong-Alhena-Product-Marketing-Manager-Resume.pdf"
    if is_alhena
    else "output/pdf/Haylie-Wong-Ashby-Product-Support-Specialist-APAC-Resume.pdf"
    if is_ashby_support
    else "output/pdf/Haylie-Wong-Ashby-Senior-Product-Designer-Resume.pdf"
    if is_ashby_designer
    else "output/pdf/Haylie-Wong-ICONIQ-Resume.pdf"
    if is_iconiq
    else "output/pdf/Haylie-Wong-Bobyard-Resume.pdf"
    if is_bobyard
    else "output/pdf/Haylie-Wong-Resume.pdf"
)
output_path.parent.mkdir(parents=True, exist_ok=True)

ink = HexColor("#000000")
document = SimpleDocTemplate(
    str(output_path),
    pagesize=letter,
    rightMargin=.7 * inch,
    leftMargin=.7 * inch,
    topMargin=.28 * inch,
    bottomMargin=.2 * inch,
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=27, leading=28, textColor=ink, spaceAfter=4))
styles.add(ParagraphStyle(name="Role", fontName="Helvetica", fontSize=8.2, leading=10.4, textColor=ink, spaceAfter=4))
styles.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=11.4, leading=13, textColor=ink, spaceBefore=4, spaceAfter=2, uppercase=True))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=8.1, leading=9.8, textColor=ink, spaceAfter=2))
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
        (
            "<b>OFFICE COORDINATOR</b>"
            if is_iconiq
            else "<b>PRODUCT DESIGNER | AI-ASSISTED PRODUCTS & SYSTEMS</b>" if is_sierra_designer
            else "<b>PRODUCT MANAGER | PRODUCT DESIGN & OPERATIONS</b>" if is_mochi_pm
            else "<b>OPERATIONS & CUSTOMER SUPPORT</b>" if is_rocket_operations
            else "<b>PRODUCT MARKETING & COMMUNICATIONS</b>" if is_alhena
            else "<b>PRODUCT SUPPORT SPECIALIST</b>" if is_ashby_support else "<b>PRODUCT DESIGNER</b>"
        )
        + "<br/>"
        + (
            "RELOCATING TO SAN FRANCISCO, CA | HOUSING SECURED"
            if is_iconiq or is_alhena or is_rocket_operations or is_mochi_pm or is_sierra_designer
            else "SINGAPORE" if is_ashby_support else "TORONTO, ON"
        )
        + "<br/>"
        "<link href=\"mailto:hayliewsw@gmail.com\">hayliewsw@gmail.com</link> | "
        "<link href=\"https://www.linkedin.com/in/hayliewsw/\">linkedin.com/in/hayliewsw</link> | "
        "<link href=\"https://hayliewsw.github.io/portfolio/\">hayliewsw.github.io/portfolio/</link>",
        styles["Role"],
    ),
    Paragraph("PROFILE", styles["Section"]),
    Paragraph(
        (
            "Organized, service-minded professional with experience coordinating executive priorities, confidential information, stakeholder communication, and day-to-day operational workflows. I bring a proactive approach to maintaining clear systems, welcoming experiences, and dependable follow-through across teams. Relocating to San Francisco with housing secured and seeking employer-sponsored U.S. work authorization."
            if is_iconiq
            else "Product designer with four years of experience creating customer-facing mobile, web, and workflow products from ambiguous problems through research, systems, prototypes, detailed specifications, testing, and launch. I combine interaction and visual craft with a systems mindset, working closely with product and engineering to make complex behavior clear and buildable. As an independent creator and studio co-founder, I also use AI-assisted coding to prototype original products, test ideas early, and iterate from real feedback. Native Cantonese speaker. Relocating to San Francisco with housing secured and seeking employer-sponsored U.S. work authorization."
            if is_sierra_designer
            else "Product professional with four years of experience taking digital products from ambiguous customer and business needs through discovery, interaction and workflow definition, detailed specifications, validation, and launch. My background in product design gives me a hands-on understanding of user needs and engineering delivery, while my independent builds demonstrate fast scoping, AI-assisted execution, and ownership. I am transitioning into product management to own not only how solutions work, but which problems teams prioritize and the outcomes they pursue. Relocating to San Francisco with housing secured and seeking employer-sponsored U.S. work authorization."
            if is_mochi_pm
            else "Customer-focused operations professional with experience turning complex information, unclear questions, and detailed workflows into clear next steps. Across senior copywriting, B2C product design, and executive support, I have created accurate customer-facing communication, organized competing priorities, investigated edge cases, and translated user feedback into practical improvements. I bring calm written communication, product curiosity, and dependable follow-through to helping members get value from digital tools. Relocating to San Francisco with housing secured and seeking employer-sponsored U.S. work authorization."
            if is_rocket_operations
            else "Product communicator and senior copywriter with four years of digital product experience spanning shipped mobile and web products, customer research, messaging, and cross-functional delivery. I translate complex products and user needs into clear, audience-aware stories. My work combines hands-on content creation, product thinking, stakeholder alignment, and AI-assisted prototyping. Relocating to San Francisco with housing secured and seeking employer-sponsored U.S. work authorization."
            if is_alhena
            else "Customer-focused product professional with experience turning unclear questions, detailed information, and operational workflows into clear next steps. Across product design, executive support, and client-sensitive communications, I have documented processes, tested product experiences, worked through edge cases, and partnered across product, engineering, marketing, and data. I bring calm written communication, strong product curiosity, and careful follow-through to helping users get value from software."
            if is_ashby_support
            else
            "Digital product designer with four years of UX/UI and product experience across mobile, responsive web, workflow tools, and game UX. I turn detailed information and operational work into clear, practical digital experiences. My end-to-end practice spans research, information architecture, user flows, prototypes, interface systems, production specifications, and usability testing. I collaborate closely with stakeholders and developers to move from ambiguity to useful, buildable products."
            if is_bobyard or is_ashby_designer
            else "Digital product designer with four years of UX/UI and product experience across mobile, responsive web, and game UX. I turn complex workflows, information, and interaction systems into clear, practical experiences. My end-to-end practice spans research, information architecture, user flows, prototypes, interface systems, production specifications, and usability testing. I collaborate closely with stakeholders and developers to translate operational needs into dependable customer journeys."
        ),
        styles["Profile"],
    ),
    Paragraph("CORE SKILLS", styles["Section"]),
    Paragraph(
        (
            "&bull; Office and operations coordination &nbsp;&nbsp;&nbsp; &bull; Executive support &nbsp;&nbsp;&nbsp; &bull; Vendor and stakeholder communication<br/>"
            "&bull; Confidential information handling &nbsp;&nbsp;&nbsp; &bull; Calendar and priority management &nbsp;&nbsp;&nbsp; &bull; Microsoft Office Suite<br/>"
            "&bull; Notion &nbsp;&nbsp;&nbsp; &bull; Documentation and process organization &nbsp;&nbsp;&nbsp; &bull; Customer service"
            if is_iconiq
            else "&bull; End-to-end product design &nbsp;&nbsp;&nbsp; &bull; Interaction & visual design &nbsp;&nbsp;&nbsp; &bull; Customer research & usability testing<br/>"
            "&bull; Design systems & reusable components &nbsp;&nbsp;&nbsp; &bull; Complex workflows & edge states &nbsp;&nbsp;&nbsp; &bull; Rapid prototyping<br/>"
            "&bull; Figma &nbsp;&nbsp;&nbsp; &bull; AI-assisted coding &nbsp;&nbsp;&nbsp; &bull; GitHub workflows &nbsp;&nbsp;&nbsp; &bull; HTML/CSS familiarity &nbsp;&nbsp;&nbsp; &bull; Cantonese (native)"
            if is_sierra_designer
            else "&bull; Product discovery & problem definition &nbsp;&nbsp;&nbsp; &bull; Customer research & insight synthesis &nbsp;&nbsp;&nbsp; &bull; Workflow design<br/>"
            "&bull; Detailed product specifications &nbsp;&nbsp;&nbsp; &bull; Cross-functional delivery &nbsp;&nbsp;&nbsp; &bull; Product QA & edge-state thinking<br/>"
            "&bull; AI-assisted prototyping & building &nbsp;&nbsp;&nbsp; &bull; Figma & Notion &nbsp;&nbsp;&nbsp; &bull; GitHub workflows &nbsp;&nbsp;&nbsp; &bull; HTML/CSS familiarity"
            if is_mochi_pm
            else "&bull; Written customer communication &nbsp;&nbsp;&nbsp; &bull; Complex-topic explanation &nbsp;&nbsp;&nbsp; &bull; Workflow and priority management<br/>"
            "&bull; Customer empathy & active listening &nbsp;&nbsp;&nbsp; &bull; Issue and feedback synthesis &nbsp;&nbsp;&nbsp; &bull; Process documentation<br/>"
            "&bull; B2C product experience &nbsp;&nbsp;&nbsp; &bull; Product QA and edge-state thinking &nbsp;&nbsp;&nbsp; &bull; Cross-functional collaboration &nbsp;&nbsp;&nbsp; &bull; Notion"
            if is_rocket_operations
            else "&bull; Product messaging & positioning &nbsp;&nbsp;&nbsp; &bull; Content strategy & copywriting &nbsp;&nbsp;&nbsp; &bull; Customer research<br/>"
            "&bull; Stakeholder communication &nbsp;&nbsp;&nbsp; &bull; Insight synthesis &nbsp;&nbsp;&nbsp; &bull; Cross-functional product collaboration<br/>"
            "&bull; AI-assisted prototyping &nbsp;&nbsp;&nbsp; &bull; Usability testing &nbsp;&nbsp;&nbsp; &bull; Information architecture &nbsp;&nbsp;&nbsp; &bull; Figma & Notion"
            if is_alhena
            else "&bull; Product support mindset &nbsp;&nbsp;&nbsp; &bull; Written customer communication &nbsp;&nbsp;&nbsp; &bull; Issue and feedback synthesis<br/>"
            "&bull; Product QA and edge-state thinking &nbsp;&nbsp;&nbsp; &bull; Usability testing &nbsp;&nbsp;&nbsp; &bull; Documentation and process organization<br/>"
            "&bull; Cross-functional collaboration &nbsp;&nbsp;&nbsp; &bull; Data and workflow organization &nbsp;&nbsp;&nbsp; &bull; Figma & Notion"
            if is_ashby_support
            else "&bull; Product design &nbsp;&nbsp;&nbsp; &bull; UX/UI design &nbsp;&nbsp;&nbsp; &bull; Information architecture &nbsp;&nbsp;&nbsp; &bull; Workflow design<br/>"
            "&bull; Design systems &nbsp;&nbsp;&nbsp; &bull; Wireframes, flows & prototypes &nbsp;&nbsp;&nbsp; &bull; Responsive design<br/>"
            "&bull; Remote usability testing &nbsp;&nbsp;&nbsp; &bull; Production specifications &nbsp;&nbsp;&nbsp; &bull; Art direction & game UX"
        ),
        styles["Body"],
    ),
    Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]),
]

experience = [
    ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Co-founded a game studio; lead art direction and game UX from concepts through playtesting, partnering with development to iterate gameplay."),
    ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote", "Design and playtest small game projects, shaping interaction flows, visual systems, onboarding, and moment-to-moment feedback alongside development collaborators."),
    ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Write clear, audience-aware immigration content while handling sensitive client information with discretion and accuracy."),
    ("2023 - 2024", "Executive Assistant", "ed&c | Singapore", "Coordinated executive priorities, scheduling, communications, and operational workflows while maintaining confidentiality and keeping stakeholders aligned."),
    ("2020 - 2022", "Digital Product Designer", "abillion | Singapore", "Owned end-to-end UX for a launched profile revamp, delivering systems, flows, prototypes, specifications, and remote usability testing."),
    ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Designed responsive website experiences, translating brand and information-architecture needs into UI, prototypes, and build-ready specifications."),
]

if is_alhena:
    experience = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Shape the positioning and player experience for an independent game studio, leading art direction and game UX from concept through playtesting and partnering with development to turn feedback into product improvements."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote", "Develop and communicate original product concepts through AI-assisted prototyping, interaction design, visual storytelling, onboarding, and iterative playtesting with development collaborators."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Create clear, audience-aware content that turns complex immigration topics into useful guidance. Adapt messaging to customer needs while maintaining accuracy, discretion, and a consistent voice across sensitive communications."),
        ("2023 - 2024", "Executive Assistant", "ed&c | Singapore", "Coordinated executive priorities and communications, keeping stakeholders aligned across fast-moving operational work while handling confidential information with care."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore", "Owned end-to-end UX for a launched profile revamp. Partnered across product, engineering, marketing, and data; translated customer and stakeholder feedback into product direction, messaging hierarchy, prototypes, specifications, and launch-ready experiences."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Translated client brands, business goals, and information needs into responsive website experiences, content hierarchies, prototypes, and build-ready specifications in collaboration with project managers, clients, and developers."),
    ]

if is_rocket_operations:
    experience = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Coordinate creative priorities and feedback across an independent game studio, partnering with development to identify issues, test solutions, and improve the player experience."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote", "Design and test digital experiences, documenting issues and edge cases, organizing iterative work, and turning participant feedback into clearer onboarding and interaction flows."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Turn complex, high-stakes immigration information into clear, accurate, audience-aware guidance. Adapt written communication to individual customer needs while handling sensitive information with discretion and care."),
        ("2023 - 2024", "Executive Assistant", "ed&c | Singapore", "Managed competing executive priorities, schedules, communications, and operational workflows. Maintained careful follow-through across open items while keeping confidential information organized and stakeholders aligned."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore", "Worked within a B2C technology company to improve customer-facing product experiences. Investigated user needs and edge states, documented flows and specifications, partnered across product, engineering, marketing, and data, and synthesized usability feedback into actionable improvements."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Translated client needs and complex information into clear responsive experiences, coordinating feedback and detailed handoffs with stakeholders, project managers, and developers."),
    ]

if is_mochi_pm:
    experience = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Co-founded an independent game studio and lead product definition, game UX, and art direction from concept through iterative playtesting. Set priorities with development, translate feedback into product decisions, and coordinate implementation through GitHub."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote", "Originate, scope, and prototype interactive products using Figma, Godot, GitHub, and AI-assisted coding. Define workflows and onboarding, test early versions, document issues, and iterate with development collaborators."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Translate complex, high-stakes information into clear, accurate, audience-aware guidance, strengthening the communication and structured thinking required for product requirements and stakeholder alignment."),
        ("2023 - 2024", "Executive Assistant", "ed&c | Singapore", "Coordinated executive priorities, communications, and operational workflows across competing workstreams while maintaining confidentiality, organization, and consistent follow-through."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore", "Owned end-to-end UX for a launched profile revamp across personal, social, collection, settings, empty, error, and offline states. Partnered across product, engineering, marketing, and data; translated customer and stakeholder needs into flows, prototypes, detailed specifications, and launch-ready experiences; validated the direction through moderated research."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Led experience definition for responsive web projects from information architecture through detailed UI and engineering handoff, translating client goals and complex content into coherent, buildable product requirements."),
    ]

if is_sierra_designer:
    experience = [
        ("2026 - Present", "Co-founder", "Oupelaye Studio | Quebec, Canada", "Co-founded an independent game studio and lead product experience, art direction, and interaction systems from concept through playtesting. Set the visual and UX direction, partner directly with development, and turn qualitative feedback into clearer product behavior."),
        ("2025 - Present", "Independent Game Designer & Art Director", "Independent projects | Remote", "Originate and prototype interactive products using Figma, Godot, GitHub, and AI-assisted coding. Shape workflows, onboarding, visual systems, and moment-to-moment feedback, testing early versions and iterating alongside development collaborators."),
        ("2023 - Present", "Senior Copywriter", "The Immigration People | Singapore", "Translate complex, high-stakes information into clear, accurate, audience-aware guidance, strengthening the written communication and language sensitivity required for human-centered AI experiences."),
        ("2020 - 2022", "Digital Product Designer", "abillion | Singapore", "Owned end-to-end UX for a launched profile revamp across personal, social, collection, settings, empty, error, and offline states. Created reusable patterns, flows, prototypes, and build-ready specifications; partnered across product, engineering, marketing, and data; and validated the experience through moderated usability testing."),
        ("2017 - 2019", "UX/UI Designer", "Decision Science | Singapore", "Designed responsive products from information architecture through high-fidelity UI and engineering handoff, translating brand and stakeholder needs into coherent page systems, interactions, prototypes, and production-ready specifications."),
    ]

for entry in experience:
    story.append(two_column_entry(*entry))

story.append(Paragraph("SELECTED PROJECTS" if not is_iconiq else "ADDITIONAL PROJECT EXPERIENCE", styles["Section"]))
projects = [
    ("01", "Inventory Management System", "INDEPENDENT | PRODUCT DESIGN | OPERATIONS", "Independently identified, designed, built, and iterated an inventory website in five days, turning CSV and Notion data into clear categories, filters, and location-aware views for tracking stock and sales."),
    ("02", "abillion Profile Revamp", "UX/UI | RESEARCH", "Sole UX designer for a launched profile revamp, defining systems, flows, prototypes, and specifications; validated before launch in UXArmy with four participants across eight tasks."),
    ("03", "Sompo Asia Website Revamp", "RESPONSIVE UI | INFORMATION ARCHITECTURE", "Designed a full regional website across desktop and mobile, translating a refreshed brand and clearer information architecture into flows, states, and production-ready specifications. <link href=\"https://www.sompo-apac.com/\">View the live website</link>."),
    ("04", "Mad John", "GAME UX | ART DIRECTION", "Co-created an in-progress card-and-puzzle game; led game UX and art direction, using six mixed-experience playtests to introduce a hands-on tutorial and refine scoring."),
    ("05", "Toadally In Love", "GAME JAM | ART DIRECTION | UX", "Led art direction and UX for a four-day puzzle-game build, creating a readable interaction system and visual world that ranked third overall among 73 entries. <link href=\"https://szzzeler.itch.io/toadally-in-love\">Play on itch.io</link>."),
]

if is_iconiq:
    projects = [
        ("01", "Personal Inventory Management System", "INDEPENDENT | OPERATIONS | INFORMATION MANAGEMENT", "Designed and built a searchable website that organizes CSV and Notion data into clear categories, filters, and location-aware views for tracking stock and sales."),
        ("02", "abillion Profile Revamp", "CROSS-FUNCTIONAL DELIVERY | LAUNCHED PRODUCT", "Partnered with product, engineering, marketing, and data to deliver a launched profile experience, coordinating feedback, testing, documentation, and handoff."),
        ("03", "Sompo Asia Website Revamp", "CLIENT COLLABORATION | RESPONSIVE DELIVERY", "Collaborated with client representatives, project management, and development to deliver a complete, responsive regional website redesign across desktop and mobile."),
    ]

if is_alhena:
    projects = [
        ("01", "abillion Profile Revamp", "SHIPPED PRODUCT | CUSTOMER RESEARCH | CROSS-FUNCTIONAL", "Led the product experience for a profile revamp from concept through launch. Gathered customer insight through eight moderated tasks with four participants, synthesized friction points, and aligned stakeholders around a clearer content and interaction system."),
        ("02", "Inventory Management System", "AI-ASSISTED BUILD | PRODUCT STORYTELLING | OPERATIONS", "Identified an operational need and designed, built, and iterated a working inventory website in five days, translating CSV and Notion data into a clear product with categories, filters, and location-aware stock and sales views."),
        ("03", "Sompo Asia Website Revamp", "BRAND COMMUNICATION | INFORMATION ARCHITECTURE", "Turned a refreshed corporate brand and complex regional content into a coherent responsive website, collaborating with client representatives, project management, and developers through delivery. <link href=\"https://www.sompo-apac.com/\">View the live website</link>."),
        ("04", "Mad John", "AI-ASSISTED PROTOTYPING | CUSTOMER FEEDBACK", "Originated and prototyped a card-and-puzzle game with AI-assisted coding; used six mixed-experience playtests to clarify onboarding, scoring, and the product's core hook."),
    ]

if is_rocket_operations:
    projects = [
        ("01", "Inventory Management System", "OPERATIONS | WORKFLOW ORGANIZATION | INDEPENDENT", "Identified an operational need and designed, built, and iterated a working inventory website in five days, turning CSV and Notion data into searchable categories, filters, and location-aware stock and sales views."),
        ("02", "abillion Profile Revamp", "B2C PRODUCT | CUSTOMER INSIGHT | LAUNCHED", "Owned the experience for a launched profile redesign and documented personal, social, collection, settings, error, offline, and empty states. Ran eight moderated tasks with four participants and translated friction into product improvements."),
        ("03", "Mad John", "ISSUE IDENTIFICATION | TESTING | ITERATION", "Used six mixed-experience playtests to identify onboarding and scoring confusion, document feedback, and introduce a hands-on tutorial that made the product easier to understand."),
    ]

if is_mochi_pm:
    projects = [
        ("01", "abillion Profile Revamp", "SHIPPED PRODUCT | DISCOVERY | CROSS-FUNCTIONAL DELIVERY", "Led the product experience from concept through release. Defined the complete state and interaction system, partnered with product, engineering, marketing, and data, and ran eight moderated tasks with four participants to identify friction and refine the direction before launch."),
        ("02", "Inventory Management System", "0-TO-1 BUILD | OPERATIONAL WORKFLOWS | AI-ASSISTED EXECUTION", "Identified an operational problem and designed, built, and iterated a working inventory product in five days, turning CSV and Notion data into searchable categories, filters, and location-aware stock and sales views."),
        ("03", "Mad John", "PRODUCT CONCEPT | ITERATION | CUSTOMER FEEDBACK", "Originated and prototyped a card-and-puzzle product with AI-assisted coding; used six mixed-experience playtests to identify onboarding and scoring friction, introduce a hands-on tutorial, and clarify the core interaction."),
    ]

if is_sierra_designer:
    projects = [
        ("01", "abillion Profile Revamp", "SHIPPED PRODUCT | SYSTEMS | CUSTOMER RESEARCH", "Sole UX designer for a launched profile redesign. Defined its interaction and state system, reusable components, and specifications; ran eight moderated tasks with four participants to refine the experience before release."),
        ("02", "Inventory Management System", "0-TO-1 WORKFLOW PRODUCT | AI-ASSISTED BUILD", "Identified, designed, built, and iterated a working inventory product in five days, turning CSV and Notion data into clear categories, filters, and location-aware stock and sales views."),
        ("03", "Mad John", "AI-ASSISTED PROTOTYPING | INTERACTION DESIGN | TESTING", "Prototyped an original game with AI-assisted coding; used six playtests to identify friction, add a hands-on tutorial, and clarify its core interaction."),
        ("04", "Sompo Asia Website Revamp", "RESPONSIVE SYSTEM | VISUAL DESIGN", "Designed a complete regional website across desktop and mobile, translating brand and complex content into coherent layouts, states, prototypes, and specifications. <link href=\"https://www.sompo-apac.com/\">Live website</link>."),
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
